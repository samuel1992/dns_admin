from flask import Blueprint, jsonify, request

from .service import RecordService


app = Blueprint('record_api', __name__)


@app.route('/', methods=['GET'])
def get_records():
    records = RecordService.get_all()
    return jsonify(records), 200


@app.route('/', methods=['POST'])
def post_record():
    record_data = request.get_json()
    record = RecordService.create(record_data)

    return jsonify(record), 201


@app.route('/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    record_data = request.get_json()
    record = RecordService.update(record_id, record_data)

    return jsonify(record), 200


@app.route('/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    record = RecordService.delete(record_id)

    return jsonify(record), 200
