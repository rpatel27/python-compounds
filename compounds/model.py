from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Compound(db.Model):
    __tablename__ = "compounds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=False, nullable=False)
    formula = db.Column(db.Text, unique=False, nullable=False)
    inchi = db.Column(db.Text, unique=False, nullable=False)
    inchi_key = db.Column(db.Text, unique=False, nullable=False)
    smiles = db.Column(db.Text, unique=False, nullable=False)
    cross_links_count = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, formula, inchi, inchi_key, smiles, cross_links):
        self.name = name
        self.formula = formula
        self.inchi = inchi
        self.inchi_key = inchi_key
        self.smiles = smiles
        self.cross_links_count = len(cross_links)
        print(f'Compound {self.name} is added.')
