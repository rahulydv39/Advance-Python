"""name = input("What is your name?")
file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()"""


names = []
with open ("name.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")