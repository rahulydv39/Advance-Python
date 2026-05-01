list_org = ["apple", "banana", "cherry"]
"""list_copy = list_org.copy()"""
# instead of .copy method we can use 
list_copy = list(list_org)
list_copy = list_org[:]

list_copy.append("doggy")

print(list_copy)
print(list_org)