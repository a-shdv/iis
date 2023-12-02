from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from business_logic import get_params, calculate_class, get_score

app = Flask(__name__)
CORS(app)
@app.route('/api/params', methods=['GET'])
def params():
    return jsonify(get_params())

@app.route('/api/calc_classes', methods=['GET'])
def calc_classes():
    return jsonify(calculate_class())

@app.route('/api/score', methods=['GET'])
def calc_score():
    return jsonify(get_score())

if __name__ == '__main__':
    app.run(debug=True)