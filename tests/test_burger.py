import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestsBurger:

    def test_set_buns(self):
        mock_bun = Mock()           
        new_burger = Burger()       
        new_burger.set_buns(mock_bun)  
        assert new_burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        new_burger = Burger()
        new_burger.add_ingredient(mock_ingredient_1)
        new_burger.add_ingredient(mock_ingredient_2)
        assert new_burger.ingredients == [mock_ingredient_1, mock_ingredient_2]

    def test_remove_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        new_burger = Burger()
        new_burger.add_ingredient(mock_ingredient_1)
        new_burger.add_ingredient(mock_ingredient_2)
        new_burger.add_ingredient(mock_ingredient_3)
        new_burger.remove_ingredient(1)
        assert new_burger.ingredients == [mock_ingredient_1, mock_ingredient_3]

    def test_move_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        new_burger = Burger()
        new_burger.add_ingredient(mock_ingredient_1)
        new_burger.add_ingredient(mock_ingredient_2)
        new_burger.add_ingredient(mock_ingredient_3)
        new_burger.move_ingredient(0,2)
        assert new_burger.ingredients == [mock_ingredient_2, mock_ingredient_3,mock_ingredient_1]
    
    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 175
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 36
        mock_ingredient_2 = Mock() 
        mock_ingredient_2.get_price.return_value = 49  # ингредиент 2 стоит 30  
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        result = burger.get_price()
        expected_price = 175 * 2 + 36 + 49
        assert result == expected_price

    def test_get_receipt(self):
        new_burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булочка с космическим кунжутом"
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "Соус"
        mock_ingredient.get_name.return_value = "Звездный"
        mock_bun.get_price.return_value = 150
        mock_ingredient.get_price.return_value = 300
        new_burger.bun = mock_bun
        new_burger.ingredients = [mock_ingredient]
        expected_receipt = '(==== Булочка с космическим кунжутом ====)\n= соус Звездный =\n(==== Булочка с космическим кунжутом ====)\n\nPrice: 600'
        assert new_burger.get_receipt() == expected_receipt
