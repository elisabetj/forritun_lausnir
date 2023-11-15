#!/usr/bin/python3

class Item:
    def __init__(self, name, category):
        self.__name = name
        self.__category = category

    def __str__(self):
        return "Name: {}, Category: {}".format(self.__name, self.__category)
    
    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def set_category(self, category):
        pass
