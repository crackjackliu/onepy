#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    删除ec卡信息
    FLASK_APP=hello.py flask run
    Running on http://localhost:5000/
"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello")
def hello1():
    return "Hello World!"
