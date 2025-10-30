#to lowercase
name="JOHn"
print(name.lower())

#slicing
sentence_one="The Dog Breed is German Shepherd"
print(sentence_one[8:24])

sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

#spacing and length
sentence="The lazy dog; ran so fast; it hit the wall"
result=sentence.split(";")
print(len(result))

#replacing , . and spacing
first_name="joh.n"
second_name="Do,e"
print(first_name.replace(".","")  +"  "+ second_name.replace(",",""))


r='["E","W","C"]'
print(r.replace(",","" ).replace("[","").replace("]","").replace('"',""))


