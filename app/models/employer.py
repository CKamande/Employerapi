from . import db

class Employer(db.Model):
    __tablename__ = 'employers'  # ✅ Plural table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=True)  # ✅ Add this line

    employees = db.relationship('Employee', backref='employer', lazy=True)
