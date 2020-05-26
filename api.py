#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request
from fake_useragent import UserAgent
import requests
app = Flask(__name__)


# define header

def set_header_user_agent():
    user_agent = UserAgent()
    return user_agent.random


@app.route('/')
def home():

    if request.args.get('url') is None:
        return 'No param??'

    _url = request.args.get('url')

    _useragent = set_header_user_agent()
    _headers = {'User-Agent': _useragent}
    req = requests.get(_url, headers=_headers, timeout=15)

    if req.status_code != requests.codes.ok:
        return 'Um... Bad request :/\n'

    return req.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

