# app/database.py
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Create the base class for models
Base = declarative_base()

# Set up the database connection (SQLite in this case)
DATABASE_URL = "sqlite:///./api.db"  # Change the URL for other databases like PostgreSQL or MySQL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create the Session class that will be used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class PredictionLog(Base):
    """
    Model to store logs of predictions in the database.
    """
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    prediction = Column(Float, nullable=False)
    input_data = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Create the tables in the database (if they don't exist)
Base.metadata.create_all(bind=engine)

# Dependency function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to log predictions into the database
def log_prediction(db_session, input_data: str, prediction: float):
    """
    Log the prediction result in the database.

    Args:
        db_session: Database session instance.
        input_data (str): Input features as a string.
        prediction (float): Prediction result.

    Returns:
        PredictionLog: The created database log entry.
    """
    db_log = PredictionLog(input_data=input_data, prediction=prediction)
    db_session.add(db_log)
    db_session.commit()
    db_session.refresh(db_log)
    return db_log
