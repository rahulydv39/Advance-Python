myset = {1, 2, 3, 1}
myset1 = set("Rahull")
print(myset1)

for _ in myset1:
    print(_)

# create an empty set
myset2 = set()
print(myset2)
# add elements im the set

myset2.add(1)
myset2.add(2)

print(myset2)

# remove element from the set

myset2.remove(1)
print(myset2)

# remove with discard method 
myset2.discard(2)
print(myset2)