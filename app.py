from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from KidneyTumorClassifier.utils.common import decodeImage
from KidneyTumorClassifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:

    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

    @app.route("/", methods=['GET'])
    @cross_origin()
    def home():
        return render_template('index.html')
    

    @app.route("/train", methods=['GET', 'POST'])
    @cross_origin()
    def trainRoute():
        os.system("dvc repro")
        # os.system("python main.py")
        return "Yeah!!! Training completed successfully"
    

    @app.route("/prediction", methods=['POST'])
    @cross_origin()
    def predictionRoute():
        image = request.json['image']
        decodeImage(image, clientApp.filename)
        result = clientApp.classifier.predict()
        return jsonify(result)




if __name__ == "__main__":
    clientApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #for AWS