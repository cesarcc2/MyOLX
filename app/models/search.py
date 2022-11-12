from sqlalchemy import Column, Integer, String
from config.config import Base

class Search(Base):
    __tablename__ = "search"
    
    id = Column(Integer, primary_key=True)
    transcript = Column(String)
    numberOfResults = Column(Integer)