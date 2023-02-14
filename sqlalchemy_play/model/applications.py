from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import Base

class Applications(Base):
    __tablename__ = "applications"

    __mapper_args__ = {
        "polymorphic_identity": "basic",
        "polymorphic_on": "type",
    }

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)

    def __repr__(self) -> str:
        return f"Application<type={self.type}, id={self.id}, name={self.name}>"

class EnhancedApplications(Applications):
    __tablename__ = "enhanced_applications"

    __mapper_args__ = {
        "polymorphic_identity": "enhanced",
    }

    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"), primary_key=True)
    clone_parent_id = Column(Integer)

    def __repr__(self) -> str:
        return f"Application<type={self.type}, id={self.id}, name={self.name}, clone_parent_id={self.clone_parent_id}>"
