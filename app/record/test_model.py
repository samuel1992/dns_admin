from fixtures import db

from .model import Record


def test_create_a_record(db):
    record = Record(qtype="A", qname="test.com", content="192.168.0.3")
    db.session.add(record)
    db.session.commit()

    assert Record.query.first() is not None
