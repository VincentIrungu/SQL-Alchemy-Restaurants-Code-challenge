from sqlalchemy import create_engine, Column, Integer, String, Table,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()
"""review = Table (
    "customer_resturant_review",
    Base.metadata,
    Column('review_id', Integer(), primary_key=True),
    Column('review_rating', Float(2)),
    Column('restaurant_id', ForeignKey('restaurants.id')),
    Column('customer_id', ForeignKey('customers.id')),
    extend_existing = True

)
"""


"""
class Restaurant(Base):

    __tablename__='restaurants'
    id=Column(Integer(), primary_key=True)
    name=Column(String())
    price=Column(Float())

    customer_review = relationship('Customer', backref = 'restaurant')
    customer = relationship('Customer', secondary ='reviews', back_populates= 'restaurant')


    def __repr__(self):
        return f"Restaurant; {self.name}"
    



   

class Customer(Base):
    __tablename__='customers'
    id=Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column (String())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_review = relationship ('Restaurants', secondary = 'reviews', back_populates= 'customer')


class Review (Base):
    __tablename__='reviews'
    id=Column(Integer(), primary_key=True)
    rating=Column(Float())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
"""
"""class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Float())

    customer_review = relationship('Customer', back_populates='restaurant')


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_review = relationship('Review', secondary='reviews', back_populates='customer')


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    rating = Column(Float())
    customer_id = Column(Integer())
    restaurant_id = Column(Integer())"""

"""class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Float())

    customer_review = relationship('Review', back_populates='restaurant')


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_review = relationship('Review', secondary='reviews', back_populates='customer')

    # Define the relationship with Review
    reviews = relationship('Review', back_populates='customer')


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    rating = Column(Float())

    # Define the foreign key relationships
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))

    # Define the relationships with Customer and Restaurant
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='customer_review')

"""

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Float())

    customer_review = relationship('Review', back_populates='restaurant')

    def __repr__(self):
        return f"Restaurant; {self.name}"


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_review = relationship('Review', primaryjoin='Customer.id == Review.customer_id', back_populates='customer')

    # Define the relationship with Review
    reviews = relationship('Review', back_populates='customer')

    def __repr__(self):
        return f"Customer; {self.first_name}{self.last_name}"

  


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    rating = Column(Float())

    # Define the foreign key relationships
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))

    # Define the relationships with Customer and Restaurant
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='customer_review')



    def __repr__(self):
        return f"Review; {self.first_name}{self.last_name}"



engine = create_engine('sqlite:///restaurants.db')

Session = sessionmaker(bind=engine)

session = Session()
Base.metadata.create_all(bind=engine)



print("................................................................................")


def review_customer (first_name:str):
    result= session.query(Customer).filter_by(first_name= first_name).all()
    return f"Your customer is {result}"

print(review_customer('Tadeo'))


def review_restaurant(name:str):
    result=session.query(Restaurant).filter_by(name=name).first()
    return f"Your restauratnt is {result}"

print(review_restaurant('The Hungry Diner'))

print(".....................................................................................")



def reviews(self):
        return session.query(Review).filter_by(restaurant_id=self.id).all()

print(reviews(1))


def customers(self):
        return session.query(Customer).join(Review).filter(Review.restaurant_id == self.id).distinct().all()
print(customers(2))
