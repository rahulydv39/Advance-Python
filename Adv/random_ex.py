# to print random value
import random

a = random.random()
print(a)

# print value in a range
b = random.uniform(1, 10)
print(b)

# print integer value

c = random.randint(1,100)
print(c)

# upper bound is not included
d = random.randrange(1, 10)
print(d)

# print number from normal distribution 
e = random.normalvariate(0, 1)
print(e)

# print random from list
mylist = list("ABCDE")
x = random.choice(mylist)
print(x)

# pick more unique elements from the list 
y = random.sample(mylist, 2)
print(y)

# if we dont want unique elemets(or choose multiple times)
z = random.choices(mylist, k=2)
print(z)

# to suffle the list
random.shuffle(mylist)
print(mylist)

#### random seed 
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

# to keep it secret
import secrets
p = secrets.randbelow(10)
print(p)

# to print random bits(0 to 15)
q = secrets.randbits(4)
print(q)

# random choice from my list that is not reproducable
r = secrets.choice(mylist)
print(r)

### random array of numbers
import numpy as np
s = np.random.rand(3,3)
print(s)

## random integer in array
t = np.random.randint(0, 10, (2,3))
print(t)

## shuffle our array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)
