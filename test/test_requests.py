# curl -X POST -F file=@images/not_from_training/feuille.jpg http://127.0.0.1:5000/predict
# curl -X POST -F file=@images/not_from_training/pierre.jpg http://127.0.0.1:5000/predict
# curl -X POST -F file=@images/not_from_training/ciseau.jpg http://127.0.0.1:5000/predict
# curl -X POST -F file=@images/not_from_training/ciseau.jpg https://image-classifier-563965826134.europe-west9.run.app/predict


import requests

# URL de l'API Flask
# url = 'http://127.0.0.1:5000/predict'

# URL GCP
url = 'https://image-classifier-563965826134.europe-west9.run.app/predict'

# URL de l'docker local
# url = 'http://127.0.0.1:8080/predict'

file_path = 'images/not_from_training/ciseau.jpg'

# Open in binary mode
with open(file_path, 'rb') as f:
    files = {'file': f}
    
    response = requests.post(url, files=files)
    
    print(response.json())
