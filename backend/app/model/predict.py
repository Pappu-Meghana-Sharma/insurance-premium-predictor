import pickle
import pandas as pd
import os

MODEL_VERSION=1.01 #this is tracked automatically by mlflow's model registry component if we use that for our ml model

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model.pkl"
)

with open(MODEL_PATH, "rb") as f:
    mlmodel = pickle.load(f)

model_loaded=mlmodel is not None

class_labels=mlmodel.classes_.tolist()
def predict_output(user_input:dict):
    user_df=pd.DataFrame([user_input])
    
    prediction=mlmodel.predict(user_df)[0]
    
    probabilities=mlmodel.predict_proba(user_df)[0] #it returns an array of shape (n_samples, n_classes) here since we have one sample-[[0.25,0.75,0]]
    confidence=max(probabilities)
    class_probs=dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))
    return {
        'prediction_category':prediction,
        'confidence':round(confidence,4),
        'class_probabilities':class_probs  
    }