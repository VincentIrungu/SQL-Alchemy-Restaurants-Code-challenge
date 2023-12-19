from models import  Restaurant, session, Customer

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

data = [{
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
print("Good work Vincent customers data seeded succesfully. Check your table")