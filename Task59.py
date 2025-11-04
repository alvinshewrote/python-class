valid_ids = [101,102,103]
user_id = [105]

if user_id  in valid_ids:
    print("access granted")
else:
    print("access denied")


variable = (49.89)
if isinstance (variable ,str):
    print("string detected")
elif isinstance (variable,int):
    print("integer detected")
else:
    print("unknown type")
    
    
    x = 7
y = 14

if x % 2 == 0:
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    if y % 2 == 0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")


