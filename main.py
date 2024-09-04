from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model('rps.h5')

# Créer l'application Flask
app = Flask(__name__)

def get_class(file_path): 
    img = image.load_img(file_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    return classes

@app.route('/', methods=['GET'])
def acceuil():
    return jsonify({'message': 'Welcome on my rock-paper-scissor api prediction'})


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        # Save picture
        file_path = "./" + file.filename
        file.save(file_path)
        
        classes = get_class(file_path)
        

        class_names = ['Paper', 'Rock', 'Scissor']
        predicted_class = class_names[np.argmax(classes)]

        return jsonify({'prediction': predicted_class})

# start Flask app
if __name__ == '__main__':
    app.run(debug=True)
