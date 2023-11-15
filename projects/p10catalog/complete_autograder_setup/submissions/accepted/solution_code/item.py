#!/usr/bin/python3


class Item:
    def __init__(self, name, category):
        """Initializes an instance of an item."""
        self.set_name(name)
        self.set_category(category)

    def __str__(self):
        """Returns a string representation of the item."""
        return f"Name: {self.__name}, Category: {self.__category}"

    def get_name(self):
        """Returns the name of the item."""
        return self.__name

    def set_name(self, name):
        """Sets the name of the item."""
        self.__name = name

    def set_category(self, category):
        """Sets the catagory of the item."""
        self.__category = category
