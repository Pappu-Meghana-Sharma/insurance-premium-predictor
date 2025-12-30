from pydantic import Field,BaseModel
from typing import Literal,Annotated,Dict

class PredictionResponse(BaseModel):
    prediction_category:Annotated[Literal['High',"Low","Medium"],Field(...,description="Prediction category of the Insurance Premium",example="High")]
    
    confidence:float=Field(...,description="Confidence with which the model has predicted the insurance premium category",example=0.452)
    
    class_probabilities:Dict[str,float]=Field(...,description="Class:prob(0 to 1)",
                                              example={"High":0.65,"Low":0.25,"Medium":0.1})
    