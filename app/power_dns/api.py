from flask import Blueprint, jsonify, request

from .service import PowerDnsService


app = Blueprint('power_dns_api', __name__)


@app.route('', methods=['POST'])
def query_record():
    query_data = request.get_json()
    method = query_data.get('method')
    qtype = query_data.get('parameters').get('qtype')

    record = PowerDnsService.get_record(method, qtype)

    return jsonify(record), 200
