correct_email = "admin@mail.com"
correct_password = "Admin@123"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    if email == correct_email and password == correct_password:
        print("Login is Successful")
      
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Invalid username or password. {remaining} attempt(s) left.")
        else:
            print("You have been blocked.")
