phonenumber_form = input("phone number: ").strip()

if phonenumber_form.startswith("+254"):
    valid_phonenumber = phonenumber_form
elif phonenumber_form.startswith("254"):
    valid_phonenumber = '+' + phonenumber_form
elif phonenumber_form.startswith("07"):
    valid_phonenumber = '+254'+ phonenumber_form[1:]
elif phonenumber_form.startswith("7"):
    valid_phonenumber = '+254'+ phonenumber_form
elif phonenumber_form.startswith("01"):
    valid_phonenumber = '+254' + phonenumber_form[1:]
elif phonenumber_form.startswith("1"):
    valid_phonenumber = '+254' + phonenumber_form
else:
    valid_phonenumber = 'invalid phone number'

print(valid_phonenumber)

    
    

    

 


