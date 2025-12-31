from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.schema.user_input import UserInput
from app.schema.prediction_response import PredictionResponse
from app.model.predict import MODEL_VERSION,predict_output,model_loaded
app=FastAPI()

#human readable        
@app.get('/')
def message():
    return {'message':"Insurance Premium Predictor API"}

#machine readable
@app.get('/health')
def health_check():
    return {
        'status':'ok',
        'model_version':MODEL_VERSION,
        'model_loaded':model_loaded
            }


@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data:UserInput):
    
    input_data={
        'age':data.age,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation,
        'bmi':data.bmi,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier   
    }
    try:
        prediction=predict_output(input_data)
        return JSONResponse(status_code=200,content=prediction)
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
