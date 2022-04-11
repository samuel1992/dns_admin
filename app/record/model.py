from extensions import db


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer(), primary_key=True)
    qtype = db.Column(db.String())
    qname = db.Column(db.String())
    content = db.Column(db.String())
    ttl = db.Column(db.Integer())
