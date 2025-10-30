numbers = {100,34,55,67,55,78}
print(numbers)
print(type(numbers))

print(55 in numbers)
print(57 in numbers)

#Add
numbers.add("five")
print(numbers)

#Update
numbers.update({1004,4000})
print(numbers)


numbers.remove(100)
print(numbers)


numbers.discard(55)
print(numbers)


numbers.discard(54)
print(numbers)

numbers.clear()
print(numbers)