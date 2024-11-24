from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Neural Network API!"}

def test_prediction():
    input_data = {"features": [[1.2, 0.8, 3.4, 2.1]]}
    response = client.post("/api/predict", json=input_data)
    assert response.status_code == 200
    assert "predictions" in response.json()
