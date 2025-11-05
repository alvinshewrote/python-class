
maths = float(input("maths: "))
eng = float(input("English: "))
swa = float(input("Kiswahili: "))
sci = float(input("Science: "))
sos = float(input("Social studies; "))
total = maths + eng+ swa + sci + sos



def get_average(total):
    average = total/5
    return average


average = get_average(total_mark)

def find_grade(average):
    if average > 79:
        return "A"
    elif average >=60:
        return "B"
    elif average >=59:
        return "C"
    elif average >=40:
        return "D"
    else:
        return "E"
    
print("enter results for the below subjects: ")

grade = find_grade(average)

print(grade)

    