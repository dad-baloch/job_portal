from sqlalchemy import engine, create_engine, text, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from dotenv import load_dotenv
import os

load_dotenv()
# it is the url of my MySQL database which is being connecting with aqlAlchemy
DATABASE_URL = os.getenv("DB_URL")
engine = create_engine(DATABASE_URL)


# IT is all i used raw sql queries.
"""
with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    # it will execute the text in as a sql command
    print(f"Type of result: {type(result)}")
    # its type is sqlalchemy.engine.cursor.cursorResult wich belong to sqlalchemy
    result_all = result.all()
    print(f"Type of result_all: {type(result_all)}")
    # but as it return the result all a list of the data
    first_result = result_all[0]
    print(f"Type of result_all[0]: {type(first_result)}")
    # instead of being a list again it shifted to a sqlalchemy.engine .row.Row but i don't know how to work with these so we need to convert this into a python dictionary

    # first_result_dict = result_all[0].__dict__ ==> it didn't worked
    first_result_dict = dict(first_result)
    print("first dict element: ", type(first_result_dict))
    result_dict = []
    for content in result_all:
        result_dict.append(dict(content))
    print(result_dict)

"""
# so here we use ORM object relational mapping

# Base will be the parent for all ORM models you define.
Base = declarative_base()


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    salary = Column(Integer, default=50000)
    currency = Column(String(10))
    responsibility = Column(String(2000))
    requirements = Column(String(2000))
    applications = relationship("Application", back_populates="job")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "location": self.location,
            "salary": self.salary,
            "currency": self.currency,
            "responsibility": self.responsibility,
            "requirements": self.requirements
        }


# jobs = session.query(Job).all()   # fresh query every time

""" 
session = Session()

jobs = session.query(Job).all()
# This runs SELECT * FROM jobs.
# It fetches all rows from jobs and returns them as a list of Job objects.
"""


class Application(Base):
    __tablename__ = "form"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    full_name = Column(String(200), nullable=False)
    email = Column(String(300), nullable=False)
    education = Column(String(2000))
    work_experience = Column(String(2000))
    resume_url = Column(String(500))
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    job = relationship("Job", back_populates="applications")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
# usign these in app.py
session = Session()


def add_form(data, job_id):
    # add forms
    form = Application(
        full_name=data["full_name"],
        email=data["email"],
        education=data["education"],
        work_experience=data["work_experience"],
        resume_url=data["resume_url"],
        job_id=job_id
    )
    session.add(form)
    session.commit()
