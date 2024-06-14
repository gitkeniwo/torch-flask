from flask import Flask, jsonify, request

from app.models.model import transform_image, get_prediction, render_prediction

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET']) # this decorator maps the / route to the root() function
def root():
    
    return jsonify({'msg' : 'Try POSTing to the /predict endpoint with an RGB image attachment'})


@app.route('/predict', methods=['POST'])
def predict():
    '''Endpoint to predict the class of an image.'''
    
    if request.method == 'POST':
        
        file = request.files['file']
        
        if file is not None:
            
            input_tensor = transform_image(file)
            prediction_idx = get_prediction(input_tensor)
            class_id, class_name = render_prediction(prediction_idx)
            
            return jsonify({'class_id': class_id, 'class_name': class_name})

def create_app():
    return app