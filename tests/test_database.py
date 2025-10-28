import pytest
from praktikum.database import Database


class TestDatabase:

    def test_available_buns_returns_list_of_three(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3

    def test_available_ingredients_returns_list_of_six(self, database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6

    @pytest.mark.parametrize('index, bun_name, bun_price', [
        (0, 'black bun', 100),
        (1, 'white bun', 200),
        (2, 'red bun', 300)
    ])
    def test_available_buns_contain_correct_data(self, database, index, bun_name, bun_price):
        buns = database.available_buns() 
        assert buns[index].get_name() == bun_name
        assert buns[index].get_price() == bun_price

    @pytest.mark.parametrize('index, ingredient_type, ingredient_name, ingredient_price', [
        (0, 'SAUCE', 'hot sauce', 100),
        (1, 'SAUCE', 'sour cream', 200),
        (2, 'SAUCE', 'chili sauce', 300),
        (3, 'FILLING', 'cutlet', 100),
        (4, 'FILLING', 'dinosaur', 200),
        (5, 'FILLING', 'sausage', 300)
    ])
    def test_available_ingredients_contain_correct_data(self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()  
        assert ingredients[index].get_type() == ingredient_type
        assert ingredients[index].get_name() == ingredient_name
        assert ingredients[index].get_price() == ingredient_price