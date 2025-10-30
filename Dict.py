person = {
    "name":"Alvin",
    "age":21,
    "address":"123 kimathi st",
    "married":False,
    "friends":{"muturi","kate"}
}
print(person)
print(type(person))

print(person["name"])
print(person["age"])
print(person.get("married"))
print(person.get("friends"))

person["id"]= 20000
print(person)

person.update({"name":"homelander","married":True,"tech capabilities":["python","sql"]})
print(person)

print(person.keys())
print(person.values())
print(person.items())


person.pop("name")
print(person)

person.popitem()
print(person)

person.clear()
print(person)