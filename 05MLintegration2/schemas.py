from pydantic import BaseModel, Field,StrictInt

class InputSchema(BaseModel):
  longitude:float
  latitude:float
  housing_median_age:int = Field(...,gt=0, description="Median age of the houses in the area")
  total_rooms:StrictInt = Field(...,gt=0, description="Total number of rooms in the area")
  total_bedrooms:StrictInt = Field(...,gt=0, description="Total number of bedrooms in the area")
  population:int = Field(...,gt=0, description="Total population in the area")
  households:StrictInt = Field(...,gt=0, description="Total number of households in the area")
  median_income:float = Field(...,gt=0, description="Median income of the households in the area")


class OutputSchema(BaseModel):
  prediction_price:float 



