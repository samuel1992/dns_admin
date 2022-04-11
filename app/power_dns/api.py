import json

from flask import Blueprint, jsonify, request, Response

from .service import PowerDnsService


app = Blueprint('power_dns_api', __name__)


@app.route('', methods=['POST'])
def query_record():
    query_data = json.loads(request.data)

    method = query_data.get('method')
    qtype = query_data.get('parameters').get('qtype')
    qname = query_data.get('parameters').get('qname')

    record = PowerDnsService.get_record(method, qtype, qname)
    data = json.dumps(record)

    return Response(data, status=200, mimetype='application/json')
