from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BITLY_ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        # Make a request to Bitly API to shorten the URL
        bitly_api_url = 'https://api-ssl.bitly.com/v4/shorten'
        headers = {
            'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        }
        payload = {
            'long_url': url
        }
        response = requests.post(bitly_api_url, headers=headers, json=payload)
        
        # Parse the response to get the shortened URL
        if response.status_code == 200:
            print("Success")
            data = json.loads(response.text)
            short_url = data['link']
            return jsonify({'short_url': short_url})
        else:
            print("Failure")
            return jsonify({'error': 'Failed to shorten URL'}), response.status_code
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
