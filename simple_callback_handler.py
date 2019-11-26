#!/usr/bin/env python3
################## flask api callback ##################
#
# This is a very basic API callback handler using flask
#
# It will receive a message and print it to stdout
#
# written by Jeremy Eglen
# license: Apache version 2.0
# Created: November 26, 2019
# Last Modified: November 26, 2019

from flask import Flask, request, jsonify

import sys
import time
import logging

MYDEBUG=False

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'This endpoint expects a POST'

@app.route('/', methods=['GET', 'POST'])
def printRequest():
    if request.method == 'GET':
        return hello()
    else:
        content = request.get_json()
        print(content)
        app.logger.info("{}::{}".format(request.remote_addr,content))
        return 'OK'


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=MYDEBUG)
