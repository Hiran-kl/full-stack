pip install sqlalchemy psycopg2 fastapi uvicorn

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, Sequence('conversation_id_seq'), primary_key=True)
    user_id = Column(Integer)
    message = Column(String(200))

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True)
    conversation_id = Column(Integer)
    content = Column(String(500))


import csv

# Replace with your actual PostgreSQL connection details
engine = create_engine('postgresql://user:password@localhost/mydatabase')

# Create tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def load_users_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = User(name=row['name'], age=int(row['age']))
            session.add(user)
        session.commit()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class MessageModel(BaseModel):
    sender_id: int
    content: str
    timestamp: str

class ConversationModel(BaseModel):
    user_id: int
    messages: List[MessageModel]

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
uvicorn your_script_name:app --reload
