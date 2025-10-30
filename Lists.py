items=["alvin",356,90,"kendi"]
print(type(items))
print(items[0])
print(items[3])
print(items[2])
print(items)
items[-1]="this is getting crazy and this is now the end of this string"
print(items)

value=[1,2,3,[4,5,6],[7,8,9,],10]
print(value[4:])


value.append(11)
print(value)
value.extend([66,"maria","kim"])
print(value)
value.insert(3,"damn")
print(value)


value.remove("kim")
print(value)
value.pop(3)
value.pop()
print(value)
value.clear()
print(value)