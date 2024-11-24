import os

# Environment-specific settings
class Config:
    MODEL_PATH = os.getenv("MODEL_PATH", "./saved_model/model.h5")
    DEBUG = os.getenv("DEBUG", True)

config = Config()
