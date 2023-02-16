import sqlalchemy
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker, with_polymorphic

from model.applications import Applications, Person

if __name__ == "__main__":
    engine = sqlalchemy.create_engine("sqlite:///../db.sqlite", echo = True)
    Session = sessionmaker(bind=engine)

    with Session() as db:
        #apps = db.query(with_polymorphic(Applications, '*'))
        #    .filter(or_(Applications.name.like('%test%'), Person.name.like('%test%')))

        """
        # Produces FROM enhanced_applications, super_applications, applications JOIN persons ON persons.id = applications.owner_id
        apps = db.query(with_polymorphic(Applications, '*'))\
            .join(Applications.owner) \
            .filter(or_(Applications.name.like('%test%'), Person.name.like('%test%')))
        """

        apps = db.query(with_polymorphic(Applications, '*'))\
            .join(Person) \
            .filter(or_(Applications.name.like('%test%')))

        """
        # Produces FROM applications LEFT OUTER JOIN enhanced_applications ON applications.id = enhanced_applications.application_id LEFT OUTER JOIN super_applications ON applications.id = super_applications.application_id JOIN persons
        apps = db.query(with_polymorphic(Applications, '*'))\
            .join(Person) \
            .filter(or_(Applications.name.like('%test%'), Person.name.like('%test%')))
        """

        for a in apps:
            print(a)
