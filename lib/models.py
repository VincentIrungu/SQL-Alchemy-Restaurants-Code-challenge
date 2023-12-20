from sqlalchemy import create_engine, Column, Integer, String, Table,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Float())

    customer_review = relationship('Review', back_populates='restaurant')


    def reviews(self):
        return session.query(Review).filter_by(restaurant_id=self.id).all()

    def customers(self):
        return session.query(Customer).join(Review).filter(Review.restaurant_id == self.id).distinct().all()



    def __repr__(self):
        return f"Restaurant; {self.name}"


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_review = relationship('Review', primaryjoin='Customer.id == Review.customer_id', back_populates='customer')

  
    reviews = relationship('Review', back_populates='customer')

    def __repr__(self):
        return f"Customer; {self.first_name}{self.last_name}"

  


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    rating = Column(Float())


    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))

    
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

print(reviews('1'))

print("..................................................")
"""def customers(self):
        return session.query(Customer).join(Review).filter(Review.restaurant_id == self.id).distinct().all()
print(customers('2'))

restaurant_instance = session.query(Restaurant).get('restaurant_id')
reviews_data = restaurant_instance.reviews()
print(reviews_data)"""

def reviews(restaurant_id):
    # Assuming restaurant_id is an integer
    restaurant_instance = session.query(Restaurant).get(restaurant_id)
    if restaurant_instance:
        return session.query(Review).filter_by(restaurant_id=restaurant_instance.restaurant_id).all()
    else:
        return None

# Example usage:
reviews_data = reviews(1)
print(reviews_data)
