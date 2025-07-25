import random

# Custom snake and ladder positions
snakes = {22: 6, 45: 30, 98: 64}
ladders = {7: 24, 21: 77, 42: 90, 40: 60}

# Initial positions
positions = {1: 0, 2: 0}


def roll_dice():
    return random.randint(1, 6)


def move(player):
    input(f"Player {player}, press Enter to roll the dice...")
    dice = roll_dice()
    print(f"🎲 Dice Score: {dice}")

    positions[player] += dice
    if positions[player] > 100:
        positions[player] -= dice
        print("❗ You need the exact number to reach 100.")

    pos = positions[player]

    if pos in snakes:
        print(f"🐍 Oh no! Snake caught you! Down from {pos} to {snakes[pos]}")
        positions[player] = snakes[pos]
    elif pos in ladders:
        print(f"🪜 Wow! You climbed a ladder! Up from {pos} to {ladders[pos]}")
        positions[player] = ladders[pos]

    print(f"🏁 Player 1 is at: {positions[1]} | Player 2 is at: {positions[2]}\n")

    if positions[player] == 100:
        print(f"🎉🎉 Player {player} wins the game! 🎉🎉")
        return True
    return False


# Game loop
print("🎮 Welcome to Snakes and Ladders!\n")
print("🐍 Snakes: 22→6, 45→30, 98→64")
print("🪜 Ladders: 7→24, 21→77, 42→90, 40→60\n")

while True:
    try:
        player_num = int(input("Enter player number (1 or 2): "))
        if player_num not in [1, 2]:
            print("❌ Invalid player number. Please enter 1 or 2.\n")
            continue
        if move(player_num):
            break
    except ValueError:
        print("❌ Please enter a valid number (1 or 2).\n")
