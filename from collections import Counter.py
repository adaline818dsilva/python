import random

snakes = {22: 6, 45: 30, 98: 64}
ladders = {7: 24, 21: 77, 42: 90, 40: 60}
pos = {1: 0, 2: 0}

def roll():
    return random.randint(1, 6)

def play(p):
    input()
    d = roll()
    print(f"Player: {p}")
    print(f"Dice Score: {d}")
    if pos[p] + d <= 100:
        pos[p] += d

    curr = pos[p]

    if curr in snakes:
        pos[p] = snakes[curr]
        print("Got Caught!")
    elif curr in ladders:
        pos[p] = ladders[curr]
        print("Got Ladder!")

    print(f"Player 1: {pos[1]}  Player 2: {pos[2]}")
    if pos[p] == 100:
        print(f"Player {p} Won It!")
        return True
    return False

while True:
    try:
        p = int(input("Enter player (1 or 2): "))
        if p not in [1, 2]:
            continue
        if play(p):
            break
    except:
        continue
