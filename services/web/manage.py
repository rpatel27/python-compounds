from flask import render_template
from flask.cli import FlaskGroup
from time import sleep
import requests
import json

from compounds import app, db, Compound

cli = FlaskGroup(app)

@cli.command("create_table")
def create_table():
    """Create a database table to store compounds"""
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("load_compounds")
def load_compounds():
    """Load all compounds from API calls into compounds table"""

    compound_list = [
        'ADP',
        'ATP',
        'STI',
        'ZID',
        'DPM',
        'XP9',
        '18W',
        '29P',
    ]

    api_url = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/'

    for compound in compound_list:
        response = requests.get(api_url + compound)
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
        sleep(1)
    
    db.session.commit()


@cli.command("get_compounds")
def get_compounds():
    """Get all compounds from compounds table"""

    compounds = Compound.query.order_by(
        Compound.id.asc()
    ).all()

    for compound in compounds:
        print(compound)

    return


if __name__ == "__main__":
    cli()
