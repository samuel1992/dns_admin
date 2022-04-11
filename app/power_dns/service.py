from record.service import RecordService

GET_DOMAIN_METADATA = 'getDomainMetadata'
LOOKUP = 'lookup'


class PowerDnsService:
    @staticmethod
    def get_record(method, qtype, qname):
        response = {'result': []}

        if method == GET_DOMAIN_METADATA:
            return response

        if method == LOOKUP:
            found_record = RecordService.filter_by({'qtype': qtype,
                                                    'qname': qname})
            response['result'] = found_record

        return response
