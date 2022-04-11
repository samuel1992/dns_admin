from flask import Blueprint, jsonify, request

from .service import RecordService


app = Blueprint('record_api', __name__)


@app.route('/', methods=['GET'])
def get_records():
    records = RecordService.get_all()
    return jsonify(records), 200
