mydict = {"name":"Rahull", "age":23, "City":"Patna"}
print(mydict, end="\n")


# creating an dictonary using dict method
mydict2 = dict(name="mayo", age=28, city="manipur")
print(mydict2)

# printing a value

value = mydict["age"]
print(value)

#append an value in dictionary

mydict["email"] = "xyz@gmail.com"
print(mydict)


# change any value 
mydict["email"] = "axyz@gmail.com"
print(mydict)

# delete an item from dictionary

del mydict["email"]
print(mydict)

#delete using pop mthod

mydict.pop("age")
print(mydict)