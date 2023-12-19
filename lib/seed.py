from models import  Restaurant, session

data = [{
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
print("Good work Vincent restaurants data seeded succesfully. Check your table")