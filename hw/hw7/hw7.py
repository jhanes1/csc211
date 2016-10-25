#!/usr/bin/env/ python3

from flask import Flask, request, render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list/<int:number>')
def list(number):
    return render_template('list.html',number=number)
