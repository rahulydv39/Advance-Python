# product

from itertools import product
a = [1, 2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))

# permutations

from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))

# for short lemgth permutation
perm2 = permutations(a, 2)
print(list(perm2))

### combinations

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a, 2) # here no repetation like (1,1)
print(list(comb))

# to print combination with replacemet

comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

# accumalte for accumulate sum
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))
# to multiply instead of sum
import operator
acc1 = accumulate(a, func=operator.mul) # to find the max func = max
print(a)
print(list(acc1))


### groupby 

from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3) # alternarive = key=lambda x: x<3
for key, value in group_obj:
    print(key, list(value))


# groupby for lists






# count function

from itertools import count, cycle, repeat

# count
for _ in count(10):
    print(_)
    if _ == 15:
        break

# cycle
a = [1,2,3]
for _ in cycle(a):
    print(_)

# repeat
"""a = [1,2,3]
for _ in repeat(1, 5):
    print(_)"""