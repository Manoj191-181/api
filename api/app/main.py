# app/main.py
from fastapi import FastAPI
from app.routes import predict_router  # Import the prediction route
from app.database import get_db  # Import the database dependency
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
origins = [
    "http://localhost:3000",  # React, Vue, or other frontend addresses
    "http://localhost",       # If you use a different local address for your frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow origins
    allow_credentials=True,
    allow_methods=["*"],    # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],    # Allow all headers
)

# Include the prediction route
app.include_router(predict_router, prefix="/api", tags=["prediction"])

@app.get("/")
async def read_root():
    """
    Root endpoint, to check if the API is working.
    """
    return {"message": "Welcome to the Neural Network API!"}

