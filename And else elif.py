grade = float(input("enter your grade:"))
if grade >= 70 and grade <=100:
    print("grade is A")
elif grade >= 60 and grade <=69:
    print("grade is B")
elif grade >= 50 and grade <=59:
    print("grade is C")
elif grade >= 40 and grade <=49:
    print("grade is D")
elif grade >= 0 and grade <=39:
    print("grade is E")
else:
    print("invalid grade")