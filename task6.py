correct_password = "admin@123"

attempts = 4

for i in range(attempts):
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access granted ")
    
    else:
        remaining = attempts - (i + 1)
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Account blocked ")
