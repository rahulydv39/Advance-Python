### shallow copy

import copy
org = [0, 1, 2, 3]
# different methods to copy
"""cpy = copy.copy(org)"""
"""cpy = org.copy()"""
"""cpy = list(org)"""
cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)

### deep copy

org1 = [[1, 2, 3], [4, 5, 6]]
cpy = copy.deepcopy(org1)
cpy[0][1] = -10
print(cpy)
print(org)
 
##shallow copy example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alex', 27)
p2 = copy.copy(p1)

p2.age = 28
print(p2.age)
print(p1.age)