import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, validates

# 1. Create an Engine
engine = create_engine('sqlite:///example.db')

# 2. Declare a Base
Base = declarative_base()

# 3. Define students table
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age =  Column(Integer)
    city = Column(String, nullable=True)

    @validates('age')
    def validate_age(self, key, value):
        if value <= 18:
            raise ValueError("Student must be older than 18")
        return value

    def __repr__(self):
        return f"<User(name='{self.name}', age='{self.age}', city='{self.city}')>"

# 4. Delete already created tables and Create the tables in the database
Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine)

# 5. Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# 6. Add an object to the session and commit the transaction
try:
    student1 = Student(name='Rahul', age=23, city=None)
    student2 = Student(name='Rakesh', age=25, city="Mumbai")
    student3 = Student(name='Rohan', age=19, city="Kolkata")
    session.add(student1)
    session.add(student2)
    session.add(student3)
    session.commit()
except ValueError as e:
    print(f"Failed to add user: {e}")
    session.rollback()

#fetch all students
from sqlalchemy import select
stmt = select(Student)
students = session.scalars(stmt).all()
for student in students:
    print(student)

#Query to update 'Rahul''s City
from sqlalchemy import update
stmt = (update(Student).where(Student.name=='Rahul').values(city='Delhi'))
session.execute(stmt)
session.commit()

#Query to delete users with age < 20
from sqlalchemy import delete
stmt = delete(Student).where(Student.age<20)
session.execute(stmt)
session.commit()

print("----After udpate----")

#fetch all students
from sqlalchemy import select
stmt = select(Student)
students = session.scalars(stmt).all()
for student in students:
    print(student)


# Close the session
session.close()