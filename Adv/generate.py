"""import random
number = random.randint(2,11)
print(number)"""

import random 
cards = ["quen", "king", "ace"]
random.shuffle(cards)

for card in cards:
    print(card)