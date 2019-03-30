#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/test")
def outside_check():
    return "this worked?"

