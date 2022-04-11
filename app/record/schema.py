from dataclasses import dataclass, asdict


# TODO: add validation fields content. Like IP format fields
@dataclass
class Record:
    qtype: str
    qname: str
    content: str
    ttl: int

    @classmethod
    def from_instance(cls, instance):
        return cls(qtype=instance.qtype,
                   qname=instance.qname,
                   content=instance.content,
                   ttl=instance.ttl)


class RecordsSchema:
    def __init__(self, records):
        if not isinstance(records, list):
            self.records = [records]
        else:
            self.records = records

    def serialize(self):
        return [asdict(Record.from_instance(r)) for r in self.records]
