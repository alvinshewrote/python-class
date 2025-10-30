#number1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)

#number2
temp1 = float(input("temperature state1: "))
temp2 = float(input("temperature state2: "))
temp3 = float(input("temperature state3: "))

if temp1 >= 30 and temp1 <= 100:
    print("temperature is too high")

elif temp2 >= 15 and temp2 <=30:
    print("normal temperature")
    
else:
    print("cold tempertaure")
    
    
#number3
    x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")
    
    
#number4
password = input("enter your password: ")
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")    


#number5
student_score = float(input("Enter student score: "))
attendance = float(input("Enter attendance percentage: "))

if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
