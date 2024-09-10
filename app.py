from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from KidneyTumorClassifier.utils.common import decodeImage
from KidneyTumorClassifier.pipeline.prediction import PredictionPipeline

