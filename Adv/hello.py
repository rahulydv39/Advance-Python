try:
    x = int(input("What is the number?"))
    print(f"x is {x}")

except ValueError:
    print("X is not an integer")