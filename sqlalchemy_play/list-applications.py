import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model.applications import Applications

if __name__ == "__main__":
    engine = sqlalchemy.create_engine("sqlite:///../db.sqlite", echo = True)
    Session = sessionmaker(bind=engine)

    with Session() as db:
        apps = db.query(Applications).all()
        for a in apps:
            print(a)
