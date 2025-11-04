products = [
    ['omo', '30kshs', '300'],
    ['milk', '50kshs', '200'],
    ['bread', '45kshs', '359'],
    ['coffee', '5kshs', '79']
]

total_stock = 0

for prod in products:
    stock = int(prod[-1]) 
    total_stock += stock

print("Total stock in the company is:", total_stock)
