from unittest.mock import patch

from fixtures import client


@patch('power_dns.service.PowerDnsService.get_record')
def test_query_record(service_get_record_mock, client):
    service_get_record_mock.return_value = [{}]

    params = {
        'method': 'lookup',
        'parameters': {
            'qtype': 'A',
            'qname': 'test.kinexon.com.',
            'remote': '192.0.2.24',
            'local': '192.0.2.1',
            'real-remote': '192.0.2.24',
            'zone-id': -1
        }
    }
    response = client.post('/dns', json=params)

    assert response.status_code == 200
