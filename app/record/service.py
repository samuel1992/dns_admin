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
    def filter_by(params):
        query = Record.query
        for attr, value in params.items():
            query = query.filter(getattr(Record, attr)==value)

        record = query.first()
        if not record:
            return []

        return RecordsSchema(record).serialize()
