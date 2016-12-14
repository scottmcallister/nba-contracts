from flask import render_template, jsonify
from nbacontracts import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/test')
def api_test():
    result = {
        "test": "test"
    }
    return jsonify(result)
