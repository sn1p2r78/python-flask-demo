import os
import sys
import socket
import requsets
from flask import Flask

import time
from flask import request
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    key = request.args.get('key')
    number = request.args.get('number')
    start0 = datetime.datetime.now(datetime.UTC)
    start = start0.strftime("%Y-%M-%dT%H:00:00.999Z")
    end = start0.strftime("%Y-%M-%dT%H:60:60.999Z")
    headers = {
                    'Content-Type': 'application/json',
                    'Api-Key': key,
                }

    json_data = {
                    'id': None,
                    'jsonrpc': '2.0',
                    'method': 'sms.mdr_full:get_list',
                    'params': {
                        'filter': {
                            'start_date': start,          
                            'end_date': end,
                            'senderid': 'Microsoft',
                            'phone': number,
                        },
                        'page': 1,
                        'per_page': 1,
                    },
                }

    response = requests.post('https://api.premiumy.net/v1.0/csv', headers=headers, json=json_data)return res
