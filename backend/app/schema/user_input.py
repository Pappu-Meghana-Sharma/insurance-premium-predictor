from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Literal, Annotated
from app.config.city_tier import tier_1_cities,tier_2_cities
class UserInput(BaseModel):
    user_age:Annotated[int,Field(...,gt=0,lt=120,description="Age of the user")]
    weight:Annotated[float,Field(...,gt=0,description="Weight of the user")]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description="Height of the user")]
    income_lpa:Annotated[float,Field(...,gt=0,lt=120,description="Annual salary of the user(in lpa)")]
    smoker:Annotated[bool,Field(...,description="Is user a smoker")]
    city:Annotated[str,Field(...,description="City of the user")]
    occupation:Annotated[Literal['retired','freelancer','student','government_job','business_owner','unemployed','private_job'],Field(...,description="Occupation of the user")]
    
    @field_validator('city')
    @classmethod
    def normalize(cls,v:str)->str:
        v=v.strip().title()  #title case 
        return v
    
    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi>30:
            return 'high'
        elif self.smoker or self.bmi>27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age(self)->str:
        if 0<=self.user_age<18:
            return "Under-Aged"
        elif 18<=self.user_age<=45:
            return "Middle-Aged"
        else:
            return "Over-Aged"
    
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3