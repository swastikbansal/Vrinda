# APi for interfacing with the mobile app
from flask import Flask, request, jsonify
import requests
import os
from urllib.parse import urlparse
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import google.generativeai as genai

import pickle
from glob import glob
from pathlib import Path

from numpy import  argmax, expand_dims 
import numpy as np

app = Flask(__name__)

utils = None

def process_img(img_path):
    model = YOLO('Model\\YOLO_V4.pt')
    result = model.predict(img_path,
                 conf=0.3,
                 save=True,
                 show=True,
                 show_conf=True,
                 project='downloads')
    


@app.route('/')
def home():
    return 'API is working'

@app.route('/predict', methods=['GET','POST'])
def predict_img():
    data = request.get_json()
    
    if not data or 'link' not in data:
        return jsonify({'error': 'No link provided'}), 400
    
    link = data['link']
    print(link)
    
    try:
        # Get the img content
        response = requests.get(link, stream=True)
        response.raise_for_status()
        
        os.makedirs('downloads', exist_ok=True)
        
        # Extract the img filename from the link
        parsed_url = urlparse(link)
        filename = os.path.basename(parsed_url.path)
        filename = f"downloads\{secure_filename(filename)}"
        
        if filename not in glob('downloads\*'):           
            # Save the img locally
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"{filename} saved")
        
        else:
            print(f"{filename} already exists")
        
        # Process the img
        prediction = process_img(filename)
        
        
        return jsonify({'prediction':prediction,'img_link':prediction}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

        
if __name__ == '__main__':    
    # Load pre-trained models from pick-le files
    
    app.run(host='127.0.0.1', port=5000, debug=True)
    