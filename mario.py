# using for loop 
"""for _ in range(3):
    print("#")"""

# using function
"""def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()"""

# clever apporach
"""def main():
    print_column(3)

def print_column(height):
   print("#\n" * height, end="")

main()
"""
# for rows

"""def main ():
    print_rows(4)

def print_rows(length):
   print("?" * length)

main()"""

# for gird 
"""def main ():
    print_square(3)

def print_square(side):
        # for each rows in square 
    for i in range(side):
        #for each brick in row
        for j in range(side):
            print("#", end="")
        print()
   
        main()
"""

def main ():
    print_square(3)

def print_square(side):
        # for each rows in square 
    for i in range(side):
        print("#"* side)

main()
   
