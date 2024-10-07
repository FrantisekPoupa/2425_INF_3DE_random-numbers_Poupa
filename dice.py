import random

def roll_die(k):
    result = random.randint(1,k)
    return result

# Otestování funkce
print(roll_die(20))  # Simulace hodu 6-hranou kostkou
