import os
import time


patterns = {
    "1": [
        "      ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   "
    ],
    "2": [
        " **** ",
        "     * ",
        "     * ",
        " ***** ",
        " *     ",
        " *     ",
        " ***** "
    ],
    "3": [
        " **** ",
        "     * ",
        "     * ",
        " ***** ",
        "     * ",
        "     * ",
        " ***** "
    ]
}


sequence = ["1", "2", "3", "3", "2", "1"]

def display_digit(digit):
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in patterns[digit]:
        print(line)
    time.sleep(0.7)


while True:
    for digit in sequence:
        display_digit(digit)