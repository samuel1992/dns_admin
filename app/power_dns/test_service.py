from unittest.mock import patch

from .service import PowerDnsService, LOOKUP


@patch('record.service.RecordService.query')
def test_get_record(record_service_query_mock):
    record = {
        'qtype': 'A',
        'qname': 'test.kinexon.com.',
        'content': '10.1.2.3',
        'ttl': 0
    }
    record_service_query_mock.return_value = [record]
    found = PowerDnsService.get_record(LOOKUP,
                                       record['qtype'],
                                       record['qname'])

    assert found == {'result': [record]}

    record_service_query_mock.assert_called_with(record['qtype'],
                                                 record['qname'])
