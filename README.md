# Shoppinglist-API

[![Coverage Status](https://coveralls.io/repos/github/EinsteinCarrey/Shoppinglist-API/badge.svg?branch=develop)](https://coveralls.io/github/EinsteinCarrey/Shoppinglist-API?branch=develop)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/35e84b6a5c0a43a49116ebffdeb80d01)](https://www.codacy.com/app/EinsteinCarrey/Shoppinglist-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=EinsteinCarrey/Shoppinglist-API&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/EinsteinCarrey/Shoppinglist-API.svg?branch=develop)](https://travis-ci.org/EinsteinCarrey/Shoppinglist-API)
[![Code Health](https://landscape.io/github/EinsteinCarrey/Shoppinglist-API/develop/landscape.svg?style=flat)](https://landscape.io/github/EinsteinCarrey/Shoppinglist-API/develop)





The Shopping-list app is an application that allows users to record and keep track of things they want to shop or buy. It allows them to keeping track of their shopping carts. This API allows clients apps to interact with the shopping-list app

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### How to run this application

## Prerequisites
* [Python 3.5](https://www.python.org/downloads/release/python-350/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)(with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) optionally)
* [Flask-Api](www.flaskapi.org)
* [Postgres](https://wiki.postgresql.org/wiki/Detailed_installation_guides)

##### Install Python

​	You can find the documentation for python **[here](https://www.python.org/)**

​	https://www.python.org/

##### Clone this repository

> https://github.com/EinsteinCarrey/Shoppinglist-API.git


##### Create a virtual environment

   ​	Use this [**guide**](http://sourabhbajaj.com/mac-setup/Python/virtualenv.html).

   ​	Activate the  virtual environment.

   1. ##### Install project dependencies

     run the command `pip -r install requirements.txt` on the command line


#### Environment Variables
    Create a .env file in the root directory and add the following:
    ```
    export FLASK_CONFIG="development"
    export db_url="postgresql://{username}:{password}@localhost/flask_api_db"
    ```


#### Migrations
    On your psql console, create your database:
    ```
    > CREATE DATABASE flask_api_db;
    ```
    Then, make and apply your Migrations
    ```
    (venv)$ python manage.py db init

    (venv)$ python manage.py db migrate
    ```

    And finally, migrate your migrations to persist on the DB
    ```
    (venv)$ python manage.py db upgrade
    ```


##### Run the server

> `python run.py`


##### Access the server using [postman](https://www.getpostman.com/)

Open a browser and access **[this location](http://127.0.0.1:5000/)**.

You can access the hosted version  **[here](https://einstein-shoppinglist-api.herokuapp.com/apidocs/)**.
https://einstein-shoppinglist-api.herokuapp.com/


##### More documentation can be found [here](https://einstein-shoppinglist-api.herokuapp.com/apidocs/)
https://einstein-shoppinglist-api.herokuapp.com/apidocs/


### Usage

| End-Points                               | Functionality                            |
| ---------------------------------------- | ---------------------------------------- |
| POST /user/login                         | Logs a user in and generates a unique token |
| POST /user/register                      | Register a user                          |
| POST /shoppinglist/                      | Create a new shopping list               |
| GET /shoppinglist/                       | List all the created shopping lists that belongs to the logged in user |
| PUT /shoppinglist/`<shopping-list id>`   | Updates the specified shopping list      |
| DELETE /shoppinglist/`<shopping-list id>` | Delete the specified shopping list       |
| POST /shoppinglist/`<shopping-list id>`/items/ | Create a new item in shopping list       |
| PUT  /items/`<item id>` | Update an item in a shopping list        |
| GET /items/ | list all items in a shopping list        |
| DELETE /item/`<item id>` | Delete a specified item in a shopping list |





## Running the tests

This code has been tested using three common python test libraries `py.test`, `unittest` and `nosetest`.

```python
# Testing in nosetest
# Navigate to the project root directory
# run the following command
nosetests tests

# Sample output
.........................................................
----------------------------------------------------------------------
Ran 20 tests in 0.459s

OK
```

### Coding style tests

This application complies with the [**PEP8**](https://www.python.org/dev/peps/pep-0008/) convention for Python. To check compliance run the following command in your command line `pep8 .` Remember to exclude your virtual environment from the scope if it is in the project directory.



## Deployment

This product is still at the development stage. I strongly discourage deploying it on a production server.

## Built With

* [**Flask-API**](www.flaskapi.org/) - An open-source  web micro-framework for python
* [**pip**](https://pypi.python.org/pypi/pip) - Python Dependency Manager
* [**PostgreSQL**](https://www.postgresql.org/) - Open source object-relational database system

## Versioning

I use [Semantic Versioning](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* [Einstein Njoroge](https://github.com/EinsteinCarrey) - You can view my profile and other works on [GitHub](https://github.com/EinsteinCarrey)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [**Hound-ci**](https://github.com/houndci-bot) - css-linting and code review
* **[Coveralls](https://coveralls.io/)** - Test Coverage checker
* **[Landscape](https://landscape.io/)** - Code quality checker