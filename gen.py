import random


moves = [
    ["F", "F\'", "F2", "f", "f\'", "f2"],
    ["F", "F\'", "F2", "f", "f\'", "f2"],
    ["B", "B\'", "B2", "b", "b\'", "b2"],
    ["L", "L\'", "L2", "l", "l\'", "l2"],
    ["R", "R\'", "R2", "r", "r\'", "r2"],
    ["U", "U\'", "U2", "u", "u\'", "u2"],
    ["D", "D\'", "D2", "d", "d\'", "d2"],
    ["M", "M\'", "M2", "M", "M\'", "M2"],
    ["E", "E\'", "E2", "E", "E\'", "E2"],
    ["S", "S\'", "S2", "S", "S\'", "S2"]
    ]

def new_scramble(scramble_length, last_index = 0 , last_group = 0):
    i = scramble_length + 1
    scramble = ""

    while i > 1:
        index = random.randint(0,5)
        group = random.randint(0,9)
        while last_index == index:
            last_index = index
            index = random.randint(0,5)
        while last_group == group:
            last_group = group
            group = random.randint(0,9)
        scramble += moves[group][index] + " "
        i -= 1
    return scramble
    
            

def random_scramble():
    i = 20 + 1
    scramble = ""
    while i > 1:
        last_index = 0
        index = random.randint(0,56)
        while last_index == index:
            last_index = index
            index = random.randint(0,56)
        else:
            last_index = index
            scramble += " " + moves[index]
        i -= 1
    return scramble

print(new_scramble(30))



    