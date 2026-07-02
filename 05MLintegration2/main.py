from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction

app =FastAPI()

@app.get('/')
def index():
  return {"welcome to ML MOdel prediction"}


@app.post('/prediction',response_model=OutputSchema)
def predict(user_input:InputSchema):
  """
  Make a prediction based on user input.

  Args:
      user_input (InputSchema): Input data for prediction.

  Returns:
      OutputSchema: Predicted value.
  """
  prediction = make_prediction(user_input.model_dump())
  return OutputSchema(prediction_price=round(prediction,2))
                      
                  

