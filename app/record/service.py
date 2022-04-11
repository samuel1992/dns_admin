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
