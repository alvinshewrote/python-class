amount = float(input("Enter transaction amount: "))
account_type = input("Enter account type (Standard or Premium): ")

if account_type == "Standard":
    if amount > 500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")
elif account_type == "Premium":
    if amount > 1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
else:
    print("Invalid account type entered.")

