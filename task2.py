user = int(input("Write a number: "))

if user % 2 != 0:
    print("The number is odd")
else:
    print("The number is even")

numbers = list(range(1, 1001))

odd = []
even = []

for number in numbers:
    if number % 2 != 0:
        odd.append(number)
    else:
        even.append(number)

print("Odd numbers:", odd)
print("Even numbers:", even)

