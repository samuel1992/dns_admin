import pytest

from fixtures import db

from .schema import RecordsSchema
from .model import Record


@pytest.fixture
def setup(db):
    record1 = Record(qtype="A", qname="test.com", content="192.168.0.3", ttl=0)
    record2 = Record(qtype="A", qname="2tst.com", content="192.168.0.4", ttl=0)
    db.session.add(record1)
    db.session.add(record2)
    db.session.commit()

    yield Record.query.all()


def test_records_schema_serialize_a_single_record(setup):
    records = setup

    records_schema = RecordsSchema(records[0])
    serialized_records = records_schema.serialize()

    for record, srecord in zip(records, serialized_records):
        assert record.id == srecord['id']
        assert record.qname == srecord['qname']
        assert record.qtype == srecord['qtype']
        assert record.content == srecord['content']
        assert record.ttl == srecord['ttl']


def test_records_schema_serialize_multiple_records(setup):
    records = setup

    records_schema = RecordsSchema(records)
    serialized_records = records_schema.serialize()

    for record, srecord in zip(records, serialized_records):
        assert record.qname == srecord['qname']
        assert record.qtype == srecord['qtype']
        assert record.content == srecord['content']
        assert record.ttl == srecord['ttl']
