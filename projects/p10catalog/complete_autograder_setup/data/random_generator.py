#!/usr/bin/python3
import random
import sys

random.seed(int(sys.argv[-1]))

module_name = sys.argv[1]
test_type = sys.argv[2]

movies = []
with open("movies.txt") as f:
    for line in f:
        movies.append(line.strip())

genres = []
with open("genres.txt") as f:
    for line in f:
        genres.append(line.strip())

catalogs = []
with open("catalogs.txt") as f:
    for line in f:
        catalogs.append(line.strip())

def random_movie_title():
    return random.choice(movies)


def random_movie_genre():
    return random.choice(genres)


def random_catalog():
    return random.choice(catalogs)


def generate_item():
    print(test_type)
    name = random_movie_title()
    category = random_movie_genre()

    print(name)
    print(category)
    if test_type == "set_name":
        print(random_movie_title())
    elif test_type == "set_category":
        print(random_movie_genre())


def add_to_catalog():
    items_to_add = random.randint(1, 5)
    print(items_to_add)
    for i in range(items_to_add):
        name = random_movie_title()
        category = random_movie_genre()
        print(name)
        print(category)
    return items_to_add


def remove_from_catalog():
    num_added = add_to_catalog()
    num_to_remove = random.randint(1, num_added)  # item to remove
    print(num_to_remove)


def clear_catalog():
    add_to_catalog()
    

def generate_catalog():
    print(test_type)
    name = random_catalog()
    print(name)
    if test_type == "set_name":
        print(random_catalog())
    elif test_type == "add":
        add_to_catalog()
    elif test_type == "remove":
        remove_from_catalog()
    elif test_type == "clear":
        clear_catalog()

           
print(module_name)
if module_name == "item":
    generate_item()
elif module_name == "catalog":
    generate_catalog()
else:
    assert False, "Invalid module name"
