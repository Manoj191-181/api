from fastapi import APIRouter, HTTPException
from app.models.model import model_instance

router = APIRouter()

@router.post("/predict")
def predict(input_data: dict):
    """
    API endpoint to make predictions using the neural network model.

    Args:
        input_data (dict): Input data containing model features.

    Returns:
        dict: Prediction results.
    """
    try:
        # Extract features from the input
        features = input_data.get("features")
        if not features:
            raise HTTPException(status_code=400, detail="Missing 'features' in request.")

        # Perform prediction
        predictions = model_instance.predict(features)

        # Return predictions
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
