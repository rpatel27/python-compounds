from flask import render_template
from flask.cli import FlaskGroup
from time import sleep
import requests
import json
import logging
import click

from compounds import app, db, Compound

cli = FlaskGroup(app)

@cli.command('get_compounds')
@click.option('--compound_name', default=None)
def get_compounds(compound_name):
    """Get all compounds from API calls in compounds table"""

    if (compound_name == ''):
        print('Empty compound name is provided')
        return
    elif (compound_name is not None):
        compound_list = [compound_name]
    else:
        compound_list = [
            'ADP', 'ATP', 'STI', 'ZID',
            'DPM', 'XP9', '18W', '29P',
        ]

    # Drop and recreate the compounds table
    db.drop_all()
    db.create_all()
    print('Table compounds is created.')

    api_url = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/'

    # Set the basic config for log handler
    logging.basicConfig(
            filename='compounds.log',
            filemode='w',
            format='%(asctime)s - %(message)s',
            level=logging.INFO
        )

    for compound in compound_list:
        response = requests.get(api_url + compound)
        logging.info('An API call is made to: {}'.format(api_url + compound))

        if response.status_code == 200:
            json_data = json.loads(response.text)
            name = json_data[compound][0]['name']
            formula = json_data[compound][0]['formula']
            inchi = json_data[compound][0]['inchi']
            inchi_key = json_data[compound][0]['inchi_key']
            smiles = json_data[compound][0]['smiles']
            cross_links = json_data[compound][0]['cross_links']

            compound_item = Compound(
                name, formula, inchi, inchi_key, smiles, cross_links
            )

            db.session.add(compound_item)
        else:
            print('Incorrect compound name is provided for API call: {}'.format(compound))

        sleep(1)
    
    db.session.commit()


@cli.command('list_compounds')
def list_compounds():
    """List all compounds from compounds table"""

    compounds = Compound.query.order_by(Compound.id.asc()).all()

    for compound in compounds:
        print(compound)


if __name__ == "__main__":
    cli()
