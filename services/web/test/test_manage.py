from flask import Flask
import click

#from compounds import app, db
from services.web.manage import get_compounds

app = Flask(__name__)

def test_get_compounds_valid_name():
    runner = app.test_cli_runner()

    result = runner.invoke(get_compounds, ['--compound_name', 'ZID'])
    assert 'ISONICOTINIC-ACETYL-NICOTINAMIDE-ADENINE DINUCLEOTIDE' in result.output


def test_get_compounds_invalid_name():
    runner = app.test_cli_runner()

    result = runner.invoke(get_compounds, ['--compound_name', 'TEST'])
    assert 'Incorrect compound name' in result.output


def test_get_compounds_empty_name():
    runner = app.test_cli_runner()

    result = runner.invoke(get_compounds, ['--compound_name', ''])
    assert 'Empty compound name' in result.output
