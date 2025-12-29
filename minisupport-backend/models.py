from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # tickets = relationship("Ticket", back_populates="owner")  # SKIP for now

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="open")
    priority = Column(String, default="medium")
    owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="tickets")  # SKIP for now
