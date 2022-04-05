import json
json_string = """
{"name": ["Jiri", "Michal"], "age": [30, 25], "city": ["Praha", "Brno"]}
"""
print(json_string)

persons = json.loads(json_string)
print(persons)

print(persons["name"])

with open("personal_data_2.json", mode="w") as json_file:
    json.dump(persons, json_file)

with open("personal_data.json", mode="w") as json_file:
    json.dump(persons, json_file, indent=4, sort_keys=True)

with open("personal_data.json") as json_file:
    my_dict = json.load(json_file)
print(json.dumps(my_dict, indent=4, sort_keys=True))

with open("personal_data_2.json", mode='r') as data_file:
    json.dump()

a = 1
b= 1565
c = "wfsdf", "Fsdf", "gwfd"



to_save = dict()
to_save['a'] = a
to_save['b'] = b
to_save['c'] = c
print(a,b,c)
