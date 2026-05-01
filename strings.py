# Reversing the string

mystring = "Hello, World"
substring = mystring[::-1]
print(substring)

for _ in mystring:
    print(_)

# to check that our string start with

print(mystring.startswith("H"))

# check our string end with something

print(mystring.endswith("World"))

# find the index of a char

print(mystring.find("lo"))

# to count the character in string

print(mystring.count("o"))

# to replace an word in string

print(mystring.replace("World", "Universe"))


# join method

my_string = 'how,are,you,doing'
my_list = my_string.split(",")
new_string = '-'.join(my_list)
print(new_string)

# to put the timer 

from timeit import default_timer as timer

start = timer()
new_string = '-'.join(my_list)
stop = timer()
print(stop-start)


# format the string
# %, .format(), f-String

# ex-1
var = "harry"
my_string2 ="the variable is %s" % var
print(my_string2)

# ex-2 (%d - for decima point and %f - for floating point)
var = 3
my_string3 ="the variable is %d" % var
print(my_string3)

# ex-3
var = 3.1234
var2 = 6.678
my_string4 ="the variable is {:.2f} and {}".format(var, var2)
# we can use this also
my_string5 =f"the variable is {var*2} and {var2}"
print(my_string5)