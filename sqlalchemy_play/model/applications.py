from sqlalchemy import Column, Integer, String
from . import Base

class Applications(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)

    def __repr__(self) -> str:
        return f"Application<type={self.type}, id={self.id}, name={self.name}>"