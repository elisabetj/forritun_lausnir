#!/usr/bin/python3


class Catalog:
    def __init__(self, name):
        """Initializes an instance of a catalog."""
        self.set_name(name)
        self.__collection = []

    def __str__(self):
        """Returns a string representation of the catalog."""
        return_str = f"Catalog {self.__name}:"
        for item in self.__collection:
            return_str += "\n\t" + str(item)
        return return_str

    def set_name(self, name):
        """Sets the name of the catalog."""
        self.__name = name

    def add(self, item):
        """Adds the given item to the catalog."""
        self.__collection.append(item)

    def remove(self, item):
        """Removes the given item from the catalog."""
        self.__collection.remove(item)

    def clear(self):
        """Clears the collection of items in the catalog."""
        self.__collection = []
