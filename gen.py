import random

moves = [
    "F", "F\'", "F2", "f", "f\'", "f2",
    "B", "B\'", "B2", "b", "b\'", "b2",
    "L", "L\'", "L2", "l", "l\'", "l2",
    "R", "R\'", "R2", "r", "r\'", "r2",
    "U", "U\'", "U2", "u", "u\'", "u2",
    "D", "D\'", "D2", "d", "d\'", "d2",
    "M", "M\'", "M2",
    "E", "E\'", "E2",
    "S", "S\'", "S2",
    "F", "F\'", "F2",
    "B", "B\'", "B2",
    "L", "L\'", "L2",
    "R", "R\'", "R2",
    "U", "U\'", "U2",
    "D", "D\'", "D2",
    ]

def random_scramble():
    i = 20
    scramble = ""
    while i > 1:
        last_index = 0
        index = random.randint(0,74)
        if last_index == index:
            last_index = index
            index = random.randint(0,74)
            scramble += " " + moves[index]
        else:
            last_index = index
            scramble += " " + moves[index]
        i -= 1
    return scramble

print(random_scramble())



    