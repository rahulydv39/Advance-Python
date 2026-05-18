# counter - gives character as key and its count as value

from collections import Counter
a = "aaaabbbbccccc"
my_counter  = Counter(a)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

# to get the first key value pair
print(my_counter.most_common(1))
# most common element 
"""print(my_counter.keys(1)[0][0])"""

# to print alll the elements
print(list(my_counter.elements()))

### namedtuple

from collections import namedtuple
point = namedtuple('point', 'x,y')
pt = point(1, -4)
print(pt.x, pt.y)


### orderdict - normal dict but remember the order

from collections import OrderedDict
ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

print(ordered_dict)

### deque

from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(0)
print(d)

d.extendleft([4,5,6])
print(d)

d.popleft()
print(d)

d.rotate(1)
print(d)