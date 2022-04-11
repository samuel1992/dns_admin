from unittest.mock import patch

from fixtures import client, db

from .model import Record


@patch('record.service.RecordService.get_all')
def test_get_records(service_get_all_mock, client, db):
    service_get_all_mock.return_value = ['something']
    response = client.get('/records/')

    assert response.status_code == 200
