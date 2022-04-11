from fixtures import db

from .model import Record
from .service import RecordService


def test_record_service_get_all(db):
    record = Record(qtype="A", qname="test.com", content="192.168.0.3")
    db.session.add(record)
    db.session.commit()

    assert len(RecordService.get_all()) == 1


def test_record_service_get_all_empty(db):
    records = RecordService.get_all()

    assert isinstance(records, list)
    assert len(records) == 0
