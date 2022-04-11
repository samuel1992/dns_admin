from unittest.mock import patch

from fixtures import client, db

from .model import Record


@patch('record.service.RecordService.get_all')
def test_get_records(service_get_all_mock, client, db):
    service_get_all_mock.return_value = ['something']
    response = client.get('/records/')

    assert response.status_code == 200


@patch('record.service.RecordService.create')
def test_create_record(service_create_mock, client, db):
    service_create_mock.return_value = [{}]
    response = client.post('/records/', json={})

    assert response.status_code == 201


@patch('record.service.RecordService.update')
def test_create_record(service_update_mock, client, db):
    service_update_mock.return_value = [{}]
    response = client.put('/records/1', json={})

    assert response.status_code == 200


@patch('record.service.RecordService.delete')
def test_delete_record(service_delete_mock, client, db):
    service_delete_mock.return_value = [1]
    response = client.delete('/records/1', json={})

    assert response.status_code == 200
