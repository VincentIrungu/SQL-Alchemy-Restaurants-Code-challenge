from models import  Restaurant, session, Customer, Review

"""data = [{
  "name": "The Hungry Diner",
  "price": 1.4
}, {
  "name": "Sizzling Steaks",
  "price": 5.7
}, {
  "name": "Flavors of India",
  "price": 4.8
}, {
  "name": "The Hungry Diner",
  "price": 2.0
}, {
  "name": "Asian Fusion",
  "price": 4.5
}, {
  "name": "Seafood Sensations",
  "price": 2.1
}]

restaurants = []

for datum in data:
    brst = Restaurant (**datum)
    restaurants.append(brst)


session.add_all(restaurants)
session.commit()
print("Good work Vincent restaurants data seeded succesfully. Check your table")"""

"""data = [{
  "first_name": "Aindrea",
  "last_name": "Cowlin",
  "restaurant_id": 1
}, {
  "first_name": "Abagail",
  "last_name": "Crassweller",
  "restaurant_id": 3
}, {
  "first_name": "Tadeo",
  "last_name": "Simka",
  "restaurant_id": 2
}, {
  "first_name": "Jerrine",
  "last_name": "Woollin",
  "restaurant_id": 2
}, {
  "first_name": "Myrilla",
  "last_name": "Rother",
  "restaurant_id": 1
}, {
  "first_name": "Osmund",
  "last_name": "Baert",
  "restaurant_id": 2
}]

customers = []

for datum in data:
    brst = Customer(**datum)
    customers.append(brst)

session.add_all(customers)
session.commit()
print("Good work Vincent customers data seeded succesfully. Check your table")"""

data = [{
  "rating": 6.8,
  "customer_id": 1,
  "restaurant_id": 1
}, {
  "rating": 4.9,
  "customer_id": 2,
  "restaurant_id": 3
}, {
  "rating": 1.6,
  "customer_id": 3,
  "restaurant_id": 2
}, {
  "rating": 1.1,
  "customer_id": 4,
  "restaurant_id": 2
}, {
  "rating": 2.8,
  "customer_id": 5,
  "restaurant_id": 1
}, {
  "rating": 5.0,
  "customer_id": 6,
  "restaurant_id": 2
}]
reviews = []

for datum in data:
    brst = Review (**datum)
    reviews.append(brst)

session.add_all(reviews)
session.commit()
print("Good work Vincent reviews data seeded succesfully. Check your table")



