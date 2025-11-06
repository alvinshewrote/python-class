def reversed_string(text):
    return text[::-1]
user = "i listen to larry june"
reversed_text = reversed_string(user)

print("Reversed string:", reversed_text)



def even_numbers(numb):
    for x in numb:
        if x %2 ==0:
            print(x)

the_list = [10,4,7,3,8,55,98,44,13,67,23,88,42,90,46]
print("the numbers in a list are: ")
even_numbers(the_list)

def square_numbers():
    square = []
    for x in range(1,31):
        square.append(x ** 2)
    return square

answer = square_numbers()

print("the squares are:", answer)