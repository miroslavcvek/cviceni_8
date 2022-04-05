import numpy as np

duck_family = {"Huey", "Dewey", "Louie", "Louie"}
print(duck_family)


my_bool = "Dewey" in duck_family

duck_family.add("Daisy")
duck_family.remove("Huey")
member = duck_family.pop()

visitor_ip = ["198.125.1.000", "198.253.100.100", "120.5.5.5", "53.130.0.0", "120.5.5.5"]

def number_of_unique_items(list_of_items):
    unique_items = []
    for item in list_of_items:
        if item not in unique_items:
            unique_items.append(item)

    unique_ammount = len(unique_items)

    return unique_ammount, unique_items

def number_of_unique_items_set(list_of_items):
    unique_items = list(set(list_of_items))
    unique_ammount = len(unique_items)

print(number_of_unique_items(visitor_ip))
print(number_of_unique_items_set(visitor_ip))


balads = {("Led Zeppelin", "Stairway to Heaven"),
("Metallica", "Fade to Black"),
("Nirvana", "The Man Who Sold the World"),
("Guns N Roses", "Patience"),
("Nirvana", "Heart Shaped Box")}
favourite = {("Nirvana", "The Man Who Sold the World"),
("Metallica", "Fade to Black"),
("Kiss", "Detroit Rock City")}

print(balads.union(favourite))
print((balads.intersection(favourite)))
print(balads.difference(favourite))

def operations_on_sets(set_1, set_2):
    monday_playlist = set_1.intersection(set_2)
    tuesday_playlist = set_2.difference(set_1)

    return monday_playlist, tuesday_playlist

print(operations_on_sets(balads, favourite))