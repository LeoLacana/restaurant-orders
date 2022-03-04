from src.inventory_control import InventoryControl


def test_validate_updated_the_quantity_in_stock():
    inventory = InventoryControl()
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    hamburguer = inventory.get_quantities_to_buy()
    total_ingredients = {
        "pao": 2,
        "carne": 2,
        "queijo": 2,
        "molho": 0,
        "presunto": 0,
        "massa": 0,
        "frango": 0,
    }
    assert hamburguer == total_ingredients


def test_validate_buy_all_stock_of_burger():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        count += 1
    hamburguer = ingredients.get_quantities_to_buy()
    total_ingredients = {
        "pao": 50,
        "carne": 50,
        "queijo": 50,
        "molho": 0,
        "presunto": 0,
        "massa": 0,
        "frango": 0,
    }
    assert hamburguer == total_ingredients


def test_validate_buy_a_amount_greater_than_the_minimum():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        ingredients.add_new_order("maria", "pizza", "terça-feira")
        count += 1
    hamburguer_pizza = ingredients.add_new_order(
        "jorge", "hamburguer", "terça-feira"
    )
    assert hamburguer_pizza is False


def test_validate_shared_ingredient():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        ingredients.add_new_order("maria", "pizza", "terça-feira")
        count += 1
    hamburguer_pizza = ingredients.get_quantities_to_buy()
    total_ingredients = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 0,
        "massa": 50,
        "frango": 0,
    }
    assert hamburguer_pizza == total_ingredients


def test_list_all_dishes_with_ingredients():
    ingredients = InventoryControl()
    ingredients.add_new_order("jorge", "coxinha", "terça-feira")
    dishes = ingredients.get_available_dishes()
    assert dishes == {"hamburguer", "pizza", "misto-quente", "coxinha"}


def test_do_not_list_dishes_without_ingredients():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "coxinha", "terça-feira")
        count += 1
    dishes = ingredients.get_available_dishes()
    assert dishes == {"hamburguer", "misto-quente"}
