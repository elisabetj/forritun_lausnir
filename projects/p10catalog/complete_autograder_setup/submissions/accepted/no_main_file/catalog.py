#!/usr/bin/python3
class Catalog:
    def __init__(self, name):
        self.set_name(name)
        self.__collection = []

    def __str__(self):
        return_str = f"Catalog {self.__name}:"
        for item in self.__collection:
            return_str += "\n\t" + str(item)
        return return_str

    def set_name(self, name):
        self.__name = name

    def add(self, item):
        self.__collection.append(item)

    def remove(self, item):
        self.__collection.remove(item)

    def find_item_by_name(self, name):
        for item in self.__collection:
            if item.get_name() == name:
                return item
        return None

    def clear(self):
        self.__collection = []
