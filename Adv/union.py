odds = { 1, 3, 5, 7}
even = {2, 4, 6, 8}
prime = {2, 3, 5, 7}

u = odds.union(even)
print(u)

i = odds.intersection(prime)
print(i)

u = odds.union(prime)
print(u) 

# difference between two sets

diff = odds.difference(prime)
print(diff)

# symmetric difference


symm_diff = odds.symmetric_difference(prime)
print(symm_diff)

# cheking for the subset

print(prime.issubset(odds))

# frozen set

a = frozenset([1, 2, 3])
print(a)