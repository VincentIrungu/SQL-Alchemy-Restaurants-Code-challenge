from sqlalchemy import create_engine, Column, Integer, String, Table,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()


class Restaurant(Base):

    __tablename__='restaurants'
    id=Column(Integer(), primary_key=True)
    name=Column(String())
    price=Column(Float())

    customer_review = relationship('Customer', backref = 'restaurant')


    def __repr__(self):
        return f"Restaurant; {self.name}"

class Customer(Base):
    __tablename__='customers'
    id=Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column (String())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))






engine = create_engine('sqlite:///restaurants.db')

Session = sessionmaker(bind=engine)

session = Session()
Base.metadata.create_all(bind=engine)