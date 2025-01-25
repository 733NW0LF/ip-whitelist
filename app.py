from flask import Flask, render_template, jsonify, request
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ip_info')
def get_ip_info():
    user_ip = request.remote_addr
    try:
        response = requests.get(f'http://ipwho.is/{user_ip}?output=json')
        data = response.json()
        return jsonify({
            'ip': data.get('ip'),
            'isp': data.get('connection', {}).get('isp'),
            'country': data.get('country')
        })
    except Exception as e:
        return jsonify({'error': 'Unable to fetch IP information'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)