# curl -X POST -F file=@images/not_from_training/feuille.jpg http://127.0.0.1:5000/predict
# curl -X POST -F file=@images/not_from_training/pierre.jpg http://127.0.0.1:5000/predict
# curl -X POST -F file=@images/not_from_training/ciseau.jpg http://127.0.0.1:5000/predict

import requests

# URL de l'API Flask
url = 'http://127.0.0.1:5000/predict'

file_path = 'images/not_from_training/feuille.jpg'

# Open in binary mode
with open(file_path, 'rb') as f:
    files = {'file': f}
    
    response = requests.post(url, files=files)
    
    print(response.json())
