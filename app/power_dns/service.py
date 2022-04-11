from record.service import RecordService

GET_DOMAIN_METADATA = 'getDomainMetadata'
LOOKUP = 'lookup'


class PowerDnsService:
    @staticmethod
    def get_record(method, qtype):
        if method == GET_DOMAIN_METADATA:
            return []

        if method == LOOKUP:
            found_record = RecordService.filter_by({'qtype': qtype,
                                                    'method': method})

            return found_record
