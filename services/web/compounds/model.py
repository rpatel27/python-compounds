from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Compound(db.Model):
    __tablename__ = "compounds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    formula = db.Column(db.String(100), unique=False, nullable=False)
    inchi = db.Column(db.String(250), unique=False, nullable=False)
    inchi_key = db.Column(db.String(50), unique=False, nullable=False)
    smiles = db.Column(db.String(100), unique=False, nullable=False)
    cross_links_count = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, formula, inchi, inchi_key, smiles, cross_links):
        self.name = name
        self.formula = formula
        self.inchi = inchi
        self.inchi_key = inchi_key
        self.smiles = smiles
        self.cross_links_count = len(cross_links)
        print(f'Compound {self.name} is added.')

    def __repr__(self):
        if len(self.name) > 13:
            name_trimmed = self.name[:10] + '...'
        else:
            name_trimmed = self.name

        if len(self.formula) > 13:
            formula_trimmed = self.formula[:10] + '...'
        else:
            formula_trimmed = self.formula

        if len(self.inchi) > 13:
            inchi_trimmed = self.inchi[:10] + '...'
        else:
            inchi_trimmed = self.inchi

        if len(self.inchi_key) > 13:
            inchi_key_trimmed = self.inchi_key[:10] + '...'
        else:
            inchi_key_trimmed = self.inchi_key

        if len(self.smiles) > 13:
            smiles_trimmed = self.smiles[:10] + '...'
        else:
            smiles_trimmed = self.smiles

        return (
            f'ID: {self.id}\n'
            f'Name: {name_trimmed}\n'
            f'Formula: {formula_trimmed}\n'
            f'Inchi: {inchi_trimmed}\n'
            f'Inchi_Key: {inchi_key_trimmed}\n'
            f'Smiles: {smiles_trimmed}\n'
            f'Cross Links Count: {self.cross_links_count}\n\n'
        )

