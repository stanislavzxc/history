from flask import Flask, render_template, request, url_for
import json
import time
import requests
import base64
from PIL import Image

app = Flask(__name__, template_folder="templates")

class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024, style = "history"):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "style": style,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)

def generate_and_save_image(myprompt):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '59DFA8E560CF3C675EA97C760270F4CE', '4693D29A1C2C945F959587CF621A538D')
    model_id = api.get_model()
    uuid = api.generate(myprompt, model_id, style = 'История России')
    images = api.check_generation(uuid)
    image_base64 = images[0]
    image_data = base64.b64decode(image_base64)
    with open("static/img/image.jpg", "wb") as file:
        file.write(image_data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/asd', methods=['POST', 'GET'])
def asd():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request
        if 'linkText' in data:  # Check if 'linkText' key exists in the JSON data
            link_text = data['linkText']  # Retrieve the value of 'linkText'
            print(link_text)  # Print the retrieved value for debugging
            generate_and_save_image(link_text)  # Perform further processing if needed
            return render_template('second.html', image=url_for('static', filename='image.jpg'))
        else:
            return "Invalid JSON data: 'linkText' key not found", 400
    else:
        return render_template('second.html', image=url_for('static', filename='image.jpg'))

if __name__ == '__main__':
    app.run(debug=True)