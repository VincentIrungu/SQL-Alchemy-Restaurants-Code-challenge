from sqlalchemy.orm import Session, Base, Customer, Restaurant

class Review(Base):
    # ... (your existing code)

    def customer(self, session: Session):
        return session.query(Customer).filter_by(id=self.customer_id).first()

    def restaurant(self, session: Session):
        return session.query(Restaurant).filter_by(id=self.restaurant_id).first()

class Restaurant(Base):
    # ... (your existing code)

    def reviews(self, session: Session):
        return session.query(Review).filter_by(restaurant_id=self.id).all()

    def customers(self, session: Session):
        return session.query(Customer




def search_barista_name (first_name: str):
    result = session.query(Baristas).filter_by(first_name = first_name).first()
    return f'Your search response is {result}'


def review_customer (fisrt_name:str):
    reselut= session.query(Customer).filter_by(first_name=first_name).all()
    return f"Your customer is {result.first_name}{result.last_name}"



