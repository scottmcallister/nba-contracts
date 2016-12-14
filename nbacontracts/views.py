from flask import render_template, jsonify
from nbacontracts import app
import pandas as pd


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def api_merged():
    df = pd.read_csv('./nbacontracts/data/merged.csv')
    response = df.to_dict(orient="records")
    return jsonify(response)


@app.route('/api/test')
def api_test():
    response = {
        "test": "test"
    }
    return jsonify(data=response)
