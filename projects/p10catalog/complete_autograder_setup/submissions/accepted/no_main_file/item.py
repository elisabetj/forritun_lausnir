#!/usr/bin/python3


class Item:
    def __init__(self, name, category):
        self.set_name(name)
        self.set_category(category)

    def __str__(self):
        return f"Name: {self.__name}, Category: {self.__category}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category
