from flask import Blueprint, jsonify, request


app = Blueprint('record_api', __name__)


@app.route('/', methods=['POST'])
def query_record():
    pass
