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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)