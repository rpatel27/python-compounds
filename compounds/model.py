from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Compound(db.Model):
    """Class to represent a single compound from a table in DB"""

    __tablename__ = "compounds"

    id = db.Column(db.Integer, primary_key=True)
    compound_name = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, unique=False, nullable=False)
    formula = db.Column(db.Text, unique=False, nullable=False)
    inchi = db.Column(db.Text, unique=False, nullable=False)
    inchi_key = db.Column(db.Text, unique=False, nullable=False)
    smiles = db.Column(db.Text, unique=False, nullable=False)
    cross_links_count = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(
            self, compound_name, name, formula, inchi,
            inchi_key, smiles, cross_links_count
        ):
        self.compound_name = compound_name
        self.name = name
        self.formula = formula
        self.inchi = inchi
        self.inchi_key = inchi_key
        self.smiles = smiles
        self.cross_links_count = cross_links_count
