from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security.api_key import APIKeyHeader
from mlproject.pipeline.prediction import PredictionPipeline
from typing import Union
from mlproject import logger
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Prediction Service"}


# Define the input schema using Pydantic
class Input(BaseModel):
  fixed_acidity: Union[float, int]
  volatile_acidity: Union[float, int]
  citric_acid: Union[float, int]
  residual_sugar: Union[float, int]
  chlorides: Union[float, int]
  free_sulfur_dioxide: Union[float, int]
  total_sulfur_dioxide: Union[float, int]
  density: Union[float, int]
  pH: Union[float, int]
  sulphates: Union[float, int]
  alcohol: Union[float, int]


API_KEY = "DUK_90"
API_KEY_NAME = "API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)
# Security dependency
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")


@app.post('/predict/')
async def make_prediction(input_data: Input, api_key: str = Depends(verify_api_key)):
    try: 
        # Prepare the input for the model
        input_features = [
            input_data.fixed_acidity,
            input_data.volatile_acidity,
            input_data.citric_acid,
            input_data.residual_sugar,
            input_data.chlorides,
            input_data.free_sulfur_dioxide,
            input_data.total_sulfur_dioxide,
            input_data.density,
            input_data.pH,
            input_data.sulphates,
            input_data.alcohol,
        ]

        
        # Make a prediction
        prediction = PredictionPipeline()
        prediction=prediction.predict(data=input_features)
        return {"input": input_data.dict(), "prediction": [prediction]}
    except Exception as e: 
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/train/")
def training(api_key: str = Depends(verify_api_key)): 
    os.system("python main.py")
    return "Training Successful!"

if __name__ == "__main__": 
    os.system("uvicorn app:app --reload --port 8000")