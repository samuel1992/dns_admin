from fixtures import db

from .model import Record
from .service import RecordService


def test_record_service_get_all(db):
    record = Record(qtype="A", qname="test.com", content="192.168.0.3", ttl=0)
    db.session.add(record)
    db.session.commit()

    assert len(RecordService.get_all()) == 1


def test_record_service_get_all_empty(db):
    records = RecordService.get_all()

    assert isinstance(records, list)
    assert len(records) == 0


def test_record_service_create(db):
    data = {
      'qtype': 'A',
      'qname': 'test.kinexon.com.',
      'content': '10.1.2.3',
      'ttl': 0
    }

    record = RecordService.create(data)

    assert record


def test_record_delete(db):
    record = Record(qtype="A", qname="test.com", content="192.168.0.3", ttl=0)
    db.session.add(record)
    db.session.commit()

    records = RecordService.delete(record.id)

    assert records
    assert Record.query.first() is None


def test_record_delete_empty(db):
    records = RecordService.delete(1)

    assert not records


def test_update_record(db):
    record = Record(qtype="A", qname="test.com", content="192.168.0.3", ttl=0)
    db.session.add(record)
    db.session.commit()

    data = {
      'qtype': 'ANY',
      'qname': 'test.kinexon.com.',
      'content': '10.1.2.3',
      'ttl': 2
    }

    RecordService.update(record.id, data)

    assert record.qtype == data['qtype']
    assert record.qname == data['qname']
    assert record.content == data['content']
    assert record.ttl == data['ttl']


def test_record_filter_by_qtype_A(db):
    record = Record(qtype="A", qname="test.com", content="192.168.0.3", ttl=0)
    db.session.add(record)
    db.session.commit()

    found_record = RecordService.query('A', 'test.com')

    assert found_record[0]['qname'] == record.qname


def test_record_filter_by_qtype_ANY(db):
    record = Record(qtype="A", qname="test.com", content="192.168.0.3", ttl=0)
    db.session.add(record)
    db.session.commit()

    found_record = RecordService.query('ANY', 'test.com')

    assert found_record[0]['qname'] == record.qname


def test_record_filter_by_qtype_SOA(db):
    record = Record(
        qtype="SOA",
        qname="test.com",
        content="ns.kinexon.com info.kinexon.com 0 86400 3600 3600000 0",
        ttl=0
    )
    db.session.add(record)
    db.session.commit()

    found_record = RecordService.query('SOA', 'test.com')

    assert found_record[0]['qname'] == record.qname


def test_record_filter_by_when_does_not_found(db):
    found_record = RecordService.query('ANY', 'test.com')

    assert not found_record
