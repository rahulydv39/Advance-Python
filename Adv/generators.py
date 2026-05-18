import sys # for cal size
"""def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))"""

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num+=1
    return nums

#print(firstn(10))
#print(sum(firstn(12)))

## same thing but with generator function with less memory

def firstn_genetator(n):
    num = 0 
    while num < n:
        yield num
        num += 1

#print(sum(firstn_genetator(10)))
print(sys.getsizeof(sum(firstn(10))))
print(sys.getsizeof(firstn_genetator(10)))


# fibbonaci

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(30)
for i in fib:
    print(i)


## print even values with generator (generator object have always the less memory)

mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)

# same even as a list
mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)
    
# same even value with coverting to list

mygenerator = (i for i in range(10) if i % 2 == 0)
print(list(mygenerator))

