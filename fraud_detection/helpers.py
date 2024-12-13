import os
import joblib
from django.conf import settings

# Load models
def load_model(filename):
    model_path = os.path.join(settings.BASE_DIR, 'fraud_detection/models', filename)
    return joblib.load(model_path)

random_forest_model = load_model('random_forest_model.pkl')
fnn_model = load_model('fnn_model.pkl')
logistic_regression_model = load_model('logistic_regression_model.pkl')
