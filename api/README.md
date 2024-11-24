# Neural Network API

## Description
A FastAPI server that serves a pre-trained neural network model. The model is loaded and used for making predictions via an HTTP POST request.

## API Endpoints

### `/api/predict`
**POST**: Make predictions using the model.

#### Request Body:
```json
{
  "features": [[1.2, 0.8, 3.4, 2.1]]
}
