from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship

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
    owner_id = Column(Integer, ForeignKey('persons.id'), nullable=True)

    owner = relationship("Person",
                         uselist=False,
                         foreign_keys=[owner_id],
                         back_populates="owned_apps",
                         single_parent=True)

    def __repr__(self) -> str:
        return f"Application<type={self.type}, id={self.id}, name={self.name}>"


class EnhancedApplications(Applications):
    __tablename__ = "enhanced_applications"

    __mapper_args__ = {
        "polymorphic_identity": "enhanced",
    }

    application_id = Column(Integer, ForeignKey('applications.id'), autoincrement=True, primary_key=True)
    clone_parent_id = Column(Integer)

    def __repr__(self) -> str:
        return f"Application<type={self.type}, id={self.id}, name={self.name}, clone_parent_id={self.clone_parent_id}>"


class SuperApplications(Applications):
    __tablename__ = "super_applications"

    __mapper_args__ = {
        "polymorphic_identity": "super",
    }

    application_id: Mapped[int] = Column(Integer, ForeignKey('applications.id'), autoincrement=True, primary_key=True)
    superhero_garment = Column(String)


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    owned_apps = relationship("Applications",
                              back_populates="owner")
