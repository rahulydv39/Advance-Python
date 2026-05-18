# lambda arguments : expression

add10 = lambda x: x + 10
print(add10(5))

# to multiply also

mult = lambda x, y : x*y
print(mult(2,4))


### map function (fun, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2 , a)
print(list(b))

## sorting a list of tuples based on the second element
a = [(1,2), (3,4), (5,1)]
sorted_a = sorted(a, key = lambda x: x[1])
print(sorted_a)

### sorting a list of tuples based on the sum of the elements
a = [(1,2), (3,4), (5,1)]
sorted_a = sorted(a, key = lambda x: x[0] + x[1])
print(sorted_a)

### map(func seq) - multiply list with 2
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))
# same as map func but easier to multiply with 2
c = [x*2 for x in a ]
print(c)

### filter (func , seq) - will get only no which is divisible by 2
d = filter(lambda x: x%2==0, a)
print(list(d))
# same thing in easy way
e = [x for x in a if x%2==0]
print(e)

### reduce (func , seq) - to multiply all numbers
from functools import reduce
f = [1, 2, 3, 4, 5]
product_f = reduce(lambda x,y : x*y, a)
print(product_f)