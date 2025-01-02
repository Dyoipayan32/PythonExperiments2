from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection and create engine
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Define a model class for SQLAlchemy
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Create tables according to the model
Base.metadata.create_all(engine)

# Add a new user to the database securely
new_user = User(name='Alice', age=30)
session.add(new_user)


# Fetch user data safely with SQLAlchemy ORM
user_name = 'Alice'
query_to_delete = session.query(User).filter_by(id=User.id).first()
session.delete(query_to_delete)
session.commit()
query = session.query(User)
for user in query:
    print(f'User Found: ID {user.id}, Name {user.name}, Age {user.age}')
