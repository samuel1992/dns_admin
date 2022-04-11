from extensions import db

from .model import Record
from .schema import RecordsSchema


class RecordService:
    @staticmethod
    def get_all():
        records = Record.query.all()
        if not records:
            return records

        serialized_records = RecordsSchema(records).serialize()
        return serialized_records

    @staticmethod
    def create(record_data):
        record = Record(**record_data)
        db.session.add(record)
        db.session.commit()

        return RecordsSchema(record).serialize()

    @staticmethod
    def delete(record_id):
        record = Record.query.get(record_id)
        if not record:
            return []

        db.session.delete(record)
        db.session.commit()

        return [record_id]

    @staticmethod
    def update(record_id, record_data):
        record = Record.query.get(record_id)
        record.query.update(record_data)

        db.session.commit()

        return RecordsSchema(record).serialize()

    @staticmethod
    def query(qtype, qname):
        if qtype in ['ANY', 'A']:
            query = Record.query.filter(Record.qtype=='A',
                                        Record.qname==qname)
        else:
            query = Record.query.filter(Record.qname==qname,
                                        Record.qtype==qtype)

        record = query.first()
        if not record:
            return []

        return RecordsSchema(record).serialize()
