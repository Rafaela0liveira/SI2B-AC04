import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')

a = 1
b = 1
for q in range (50): 
    print(a, end=' ')
    b = b + a
    a = b - a
