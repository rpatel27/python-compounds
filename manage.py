from flask.cli import FlaskGroup
from time import sleep
import requests
import json
import logging
import click
from tabulate import tabulate

from compounds import app, db, Compound

cli = FlaskGroup(app)

@cli.command('get_compounds')
@click.option('--compound_name', default=None)
def get_compounds(compound_name):
    """Get all compounds from API calls in compounds table"""

    compound_list = [
        'ADP', 'ATP', 'STI', 'ZID',
        'DPM', 'XP9', '18W', '29P',
    ]

    if (compound_name == ''):
        print('Empty compound name is provided')
        return
    elif (compound_name is not None):
        if compound_name in compound_list:
            compound_list = [compound_name]
        else:
            print('Incorrect compound name is provided: {}'.format(compound_name))
            return

    # Drop and recreate the compounds table
    db.drop_all()
    db.create_all()
    print('Table compounds is created.')

    api_url = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/'

    # Set the file handler for logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s: %(asctime)s - %(message)s')
    file_handler = logging.FileHandler('compounds.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    for compound in compound_list:
        response = requests.get(api_url + compound)
        logger.info('An API call is made to: {}'.format(api_url + compound))

        if response.status_code == 200:
            json_data = json.loads(response.text)
            name = json_data[compound][0]['name']
            formula = json_data[compound][0]['formula']
            inchi = json_data[compound][0]['inchi']
            inchi_key = json_data[compound][0]['inchi_key']
            smiles = json_data[compound][0]['smiles']
            cross_links_count = len(json_data[compound][0]['cross_links'])

            compound_item = Compound(
                compound, name, formula, inchi, inchi_key, smiles, cross_links_count
            )

            db.session.add(compound_item)
            print(f'Compound {compound} is added.')
        else:
            print('Incorrect compound name is provided: {}'.format(compound))

        sleep(1)
    
    db.session.commit()
    return


def trim_str(val_str: str) -> str:
    """
    Trim the string to 10 chars
    if its length is more than 13 chars

    parameters:
        val_str: string value to be trimmed

    Returns:
        trimmed string if length is more than 13 chars
        original string if length is less than 13 chars
    """

    return val_str[:10] + '...' \
        if len(val_str) > 13 else val_str


@cli.command('list_compounds')
def list_compounds():
    """List all compounds from compounds table"""

    compounds = Compound.query.order_by(Compound.id.asc()).all()
    head = [
        'ID', 'Compound', 'Name', 'Formula', 'Inchi',
        'Inchi_Key', 'Smiles', 'Cross_Links_Count'
    ]
    compound_list = []

    for compound in compounds:
        compound_list.append([
            compound.id,
            compound.compound_name,
            trim_str(compound.name),
            trim_str(compound.formula),
            trim_str(compound.inchi),
            trim_str(compound.inchi_key),
            trim_str(compound.smiles),
            compound.cross_links_count,
        ])

    print(tabulate(compound_list, headers=head, tablefmt='grid'))
    return


if __name__ == "__main__":
    cli()
