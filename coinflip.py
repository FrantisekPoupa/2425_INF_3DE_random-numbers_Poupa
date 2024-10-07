import random

def flip_coin():
    result = random.randint(0,1)
    if result == 0:
        return "Heads"
    else:
        return "Tails"
# Otestování funkce
print(flip_coin())
