my_tuple = ("max", "delhi", 36, "max")

"""item = my_tuple[-1]
print(item)"""

"""for _ in my_tuple:
    print(_, end="-")"""

print(len(my_tuple))

# to count something in our tuple
print(my_tuple.count("max"))

# to know the index of my tuple
print(my_tuple.index("max"))

# convert tuple into list
list = list(my_tuple)
list.append("wow")
print(list)
print(my_tuple)

# convert list into tuple
my_tuple = tuple(list)
print(my_tuple)


# to know the size and of tuple and list
import sys
my_list = [0, 1, 2, "hello", "True"]
my_tuple = (0, 1, 2, "hello", "True")

print(sys.getsizeof(my_list, "bytes"))
print(sys.getsizeof(my_tuple, "bytes"))