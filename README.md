#https://anyatibrian.github.io/fast-food-fast/
# fast_food_fast

Fast-Food-Fast is a food delivery service app for a restaurant.

### Badges
[![Build Status](https://travis-ci.com/anyatibrian/fast-food-fast.svg?branch=ApiV1)](https://travis-ci.com/anyatibrian/fast-food-fast)
[![Maintainability](https://api.codeclimate.com/v1/badges/bc4cef4996852a26c465/maintainability)](https://codeclimate.com/github/anyatibrian/fast-food-fast/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/bc4cef4996852a26c465/test_coverage)](https://codeclimate.com/github/anyatibrian/fast-food-fast/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/anyatibrian/fast-food-fast/badge.svg?branch=ApiV1)](https://coveralls.io/github/anyatibrian/fast-food-fast?branch=ApiV1)

# APIs for Fast Food Fast

These are APIs to be used to interface the fuctionality of the Fast Food Fast application

## Functionality

- Placing order for food
- Obtaining a list of orders.
- Fetching a specific order.
- Updating the order status.

These are the endpoints

| METHOD | Endpoint          | Description                                                          | Body (json)                                                    |
| ------ | :---------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| GET    | /api/v1/orders/   | Get all orders                                                       |                                                                |
| GET    | /api/v1/orders/id | Get specific orders using an id                                      |                                                                |
| POST   | /api/v1/orders    | Place a new orders                                                   | order_title, order_description ,order_price ,delivery_location |
| PUT    | /api/v1/orders/id | Update a specific orders status to 'complete','pending','incomplete' | order_status                                                   |
|                                 |                                                                |

APIs are Hosted at https://fast-food-fast-ab.herokuapp.com/api/v1/orders

Sample get all orders

## Setting Up for Development

These are instructions for setting up Fast Food Fast app in a development enivornment.

### Prerequisites

- Python 3.6

- Make a directory on your computer and a virtual environment

  ```
  $ mkdir fast-food-fast
  ```

- Prepare the virtual environment

  ```
  $ pip install virtualenv
  $ virtualenv venv
  ```

- Clone the project repo

  ```
  $ git clone https://github.com/anyatibrian/fast-food-fast.git
  ```

* switch to ApiV1 branch

  ```
  $ git checkout ApiV1
  ```

* Install necessary requirements

  ```
  $ pip install -r requirements.txt
  ```

* Run development server
  ```
  $ python app.py
  ```

This site should now be running at http://localhost:5000

### Run Tests

- Make sure pytest is installed

  ```
  $ py.test
