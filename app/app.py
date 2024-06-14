from flask import Flask, jsonify, request, render_template, current_app

from app.models.model import transform_image, get_prediction, render_prediction

app = Flask(__name__)

@app.route('/', methods=['GET']) # this decorator maps the / route to the root() function
def root():
    'Try POSTing to the /predict endpoint with an RGB image attachment'
    
    # serve a simple html page at templates/index.html
    return current_app.send_static_file('index.html')


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