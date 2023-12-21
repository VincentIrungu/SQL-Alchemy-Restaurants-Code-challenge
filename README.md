# Code-challenge

Barister-Meal Finder is a Python application built using SQLAlchemy, offering efficient management of restaurant data. This project includes three main classes: Restaurant, Customer, and Review. Each class plays a crucial role in maintaining a comprehensive database schema.

## Key Features

1. **Restaurant Class:**
    - **Attributes:**
        - `id`: Unique identifier for each restaurant.
        - `name`: Name of the restaurant.
        - `price`: Price level indicator.
    - **Functionality:**
        - Manages restaurant information.
        - Tracks associated reviews.
        - Handles relationships with customers.

2. **Customer Class:**
    - **Attributes:**
        - `id`: Unique identifier for each customer.
        - `first_name` and `last_name`: Customer's name.
    - **Functionality:**
        - Captures customer details.
        - Manages customer reviews and associated restaurants.
        - Determines the customer's favorite restaurant.

3. **Review Class:**
    - **Attributes:**
        - `id`: Unique identifier for each review.
        - `rating`: Numeric rating provided by the customer.
    - **Functionality:**
        - Represents a customer's review for a specific restaurant.

4. **Database Schema:**
    - Defines relationships between restaurants, customers, and reviews.
    - Enables seamless data management and retrieval.

## Getting Started

### Installation:

1. Clone the repository:
git clone https://github.com/your-username/your-repo.git

markdown
Copy code

2. Install dependencies:
pip install -r requirements.txt

markdown
Copy code

### Usage:

1. Execute `python models.py` to initialize the database and classes.
2. Explore `models.py` for sample operations, including adding reviews and identifying the fanciest restaurant.

### Customization:

Adapt the classes and methods to suit specific project requirements.

## Dependencies

- SQLAlchemy

## Contributors

- [Vincent Irungu Rugundu]

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
 