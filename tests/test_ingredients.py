import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price_returns_correct_price(self, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
        assert isinstance(ingredient.get_price(), float)

    def test_get_name_returns_correct_name(self, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    def test_get_type_returns_correct_type(self, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type