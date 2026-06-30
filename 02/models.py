from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Optional,Literal


class patient(BaseModel):

    id:Annotated[str,Field(...,description='the ID of patient',example='P001')]

    name:Annotated[str,Field(...,description='the name of patient',example='John Doe')]
    city:Annotated[str,Field(...,description='the city of patient',example='New York')]
    gender:Annotated[str,Field(...,description='the gender of patient',example='Male')]
    age:Annotated[int,Field(...,gt=0,lt=101,description='the age of patient',example=30)]
    height:Annotated[float,Field(...,description='the height of patient',example=5.9)]
    weight:Annotated[float,Field(...,description='the weight of patient',example=160.5)]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi= round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self,) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
        

class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(None,description='the name of patient',example='John Doe')]
    city:Annotated[Optional[str],Field(default=None)]
    age :Annotated[Optional[int],Field(default=None,gt=0)]
    gender:Annotated[Optional[Literal['male','female']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None ,gt=0)]
    weight :Annotated[Optional[float],Field(default=None ,gt=0)]
        