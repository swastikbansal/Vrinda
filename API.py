# APi for interfacing with the mobile app
from flask import Flask, request, jsonify
import requests
import os
from urllib.parse import urlparse
from werkzeug.utils import secure_filename

from ultralytics import YOLO
import cv2
from supabase import create_client, Client
from supabase.client import ClientOptions


from glob import glob
from pathlib import Path

import numpy as np

app = Flask(__name__)

utils = None

def process_img(img_path):
    model = YOLO('Model\\YOLO_V5.pt')
    result = model.predict(img_path,
                 conf=0.3,
                 save=True,
                 show=True,
                 show_conf=False,
                 project='Vrinda_API')
    
    
    
    res = result[0]
    class_ids = res.boxes.cls.tolist()
    class_names = [ model.names[int(cid)] for cid in class_ids]
        
    annotated = res.plot()

    cv2.imwrite("result.jpg", annotated)
    
    return class_names
    
    


@app.route('/')
def home():
    return 'API is working'

@app.route('/predictImg', methods=['GET','POST'])
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
        
        
        try:        
            url: str = "https://jkkoibvrkmvyibvqrixl.supabase.co"

            key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impra29pYnZya212eWlidnFyaXhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUwNTYxODEsImV4cCI6MjA2MDYzMjE4MX0.tJqLPjvOaiPIcqwB6NdulbZfN3OsNRs2BSVct8MFkzI"
            supabase: Client = create_client(
                url, 
                key,
                options=ClientOptions(
                    postgrest_client_timeout=10,
                    storage_client_timeout=10,
                    schema="public",
                )
            )

            print("Connected to supabase")
        except Exception as e:
            return jsonify({'error': 'Error connecting to supabase'}), 500
        
        try:
            with open("result.jpg", "rb") as f:
                        response = (
                            supabase.storage\
                            .from_("images")\
                            .upload(
                                file=f,
                                path="result/result.jpg"
                            )
                        )
            print("File uploaded successfully")
        
        except Exception as e:
            return jsonify({'error': 'Error uploading file'}), 500
            
        public_url = (
        supabase.storage
            .from_("images")
            .get_public_url(f"result/{f}")
        )

        print(public_url)
        
        return jsonify({'prediction':prediction,'img_link':public_url}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

        
if __name__ == '__main__':    
    # Load pre-trained models from pick-le files
    
    app.run(host='127.0.0.1', port=5000, debug=True)
    