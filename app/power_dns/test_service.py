from unittest.mock import patch

from .service import PowerDnsService, LOOKUP


@patch('record.service.RecordService.filter_by')
def test_get_record(record_service_filter_by_mock):
    record = {
        'qtype': 'A',
        'qname': 'test.kinexon.com.',
        'content': '10.1.2.3',
        'ttl': 0
    }
    record_service_filter_by_mock.return_value = [record]
    found = PowerDnsService.get_record(LOOKUP, record['qtype'])

    assert found == [record]
