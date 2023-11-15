#!/usr/bin/python3
class Catalog:
    def __init__(self, name):
        self.__name = name
        self.__collection = []
    
    def __str__(self):
        return_str = "Catalog {}:".format(self.__name)
        for item in self.__collection:
            return_str += '\n\t' + str(item)
        return return_str

    def set_name(self, name):
        pass

    def add(self, item):
        pass
    
    def remove(self, item):
        pass

    def find_item_by_name(self, name):
        pass
            
    def clear(self):
        pass
