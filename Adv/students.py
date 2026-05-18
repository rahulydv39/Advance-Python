"""with open("studnets.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")"""

with open("studnets.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} lives in {house}")