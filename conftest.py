import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient



@pytest.fixture(params=[
    ("Межгалактическая булка", 100.0),
    ("Булочка голубая Луна", 200.0),
    ("", 0.0),  
    ("Сытная булочка", 150.5),  
])
def bun_data(request):
    return request.param


@pytest.fixture
def bun_instance(bun_data):
    name, price = bun_data
    return Bun(name, price)


@pytest.fixture
def database():
    return Database()


@pytest.fixture(params=[
    ("SAUCE", "hot sauce", 100.0),
    ("SAUCE", "sour cream", 200.0),
    ("FILLING", "cutlet", 150.0),
    ("FILLING", "dinosaur", 300.0),
])
def ingredient_data(request):
    return request.param


@pytest.fixture
def ingredient_instance(ingredient_data):
    ingredient_type, name, price = ingredient_data
    return Ingredient(ingredient_type, name, price)