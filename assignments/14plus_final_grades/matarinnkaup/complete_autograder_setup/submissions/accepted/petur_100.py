#!/usr/bin/env python3
from typing import List, Tuple, Dict


def main():
    number_of_recipes, number_of_receipts = get_problem_parameters()
    recipes = get_recipes(number_of_recipes)
    dish_tally = count_dishes(number_of_receipts)
    ingredients_used = tally_ingredients(dish_tally, recipes)
    display_result(ingredients_used)


def get_problem_parameters() -> Tuple[int]:
    """Parses the first line of input."""
    parameters = input().split()
    number_of_recipes, number_of_receipts = [int(parameter) for parameter in parameters]
    return number_of_recipes, number_of_receipts


def get_recipes(
    number_of_recipes: int,
) -> Dict[str, List[Tuple[str, int]]]:
    """Records what recipes are on offer.

    Returns a dictionary, where
        a key is the name of a recipe (unique),
        the corresponding value is a list of ingredients,
            along with the quantities of each ingredient.
    """
    recipes = {}
    for _ in range(number_of_recipes):
        add_new_recipe(recipes)

    return recipes


def add_new_recipe(recipes: Dict[str, List[Tuple[str, int]]]) -> None:
    """Reads a recipe from input and records it into the given dictionary.

    Modifies the given dictionary.
    """
    dish_name = input()
    assert dish_name not in recipes

    recipes[dish_name] = []
    number_of_ingredients = int(input())
    for _ in range(number_of_ingredients):
        add_ingredient(recipe=recipes[dish_name])


def add_ingredient(recipe: List[Tuple[str, int]]) -> None:
    """Extends the list of ingredients in the given recipe, as prescribed by the input.

    Modifies the given ingredient list.
    """
    ingredient, how_much = input().split()
    quantity = int(how_much)
    recipe.append((ingredient, quantity))


def count_dishes(number_of_receipts: int) -> Dict[str, int]:
    """Goes through a given number of receipts and records how much was sold of each dish.

    Returns a dictionary, where
        a key is the name of a dish (recipe),
        the corresponding value is a number
            indicating how often the dish was purchased.
    """
    dish_tally = {}
    for _ in range(number_of_receipts):
        tally_receipt(dish_tally)

    return dish_tally


def tally_receipt(tally: Dict[str, int]) -> None:
    """Examines one receipt, counts how much was sold of each dish, and adds it to the tally.

    Modifies the given dictionary.
    """
    number_of_entries = int(input())
    for _ in range(number_of_entries):
        dish_name, how_many = input().split()
        quantity = int(how_many)

        if dish_name not in tally:
            tally[dish_name] = 0

        tally[dish_name] += quantity


def tally_ingredients(
    dish_tally: Dict[str, int],
    recipes: Dict[str, List[Tuple[str, int]]],
) -> Dict[str, int]:
    """Counts how much was used of each ingredients, for the given batch of sales.

    Returns a dictionary, where
        a key is the name of an ingredient (unique),
        the corresponding value is the total quantity used of that ingredient.
    """
    ingredient_tally = {}
    for dish_name, how_often_bought in dish_tally.items():
        add_ingredient_for_dish(
            recipe=recipes[dish_name],
            number_of_purchases=how_often_bought,
            tally=ingredient_tally,
        )

    return ingredient_tally


def add_ingredient_for_dish(
    recipe: List[Tuple[str, int]],
    number_of_purchases: int,
    tally: Dict[str, int],
) -> None:
    """Adds the ingredient quantities used for a given dish to the tally.

    Modifies the given tally dictionary.
    Does not modify the given ingredient list (recipe).
    """
    for ingredient, quantity in recipe:
        if ingredient not in tally:
            tally[ingredient] = 0

        tally[ingredient] += quantity * number_of_purchases


def display_result(ingredients_used: Dict[str, int]) -> None:
    for ingredient, quantity in sorted(ingredients_used.items()):
        print(ingredient, quantity)


if __name__ == "__main__":
    main()
