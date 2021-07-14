""" You can find this exercise at the following website: https://www.practicepython.org/

30. Pick Word

Create a program that reads sowpods.txt and returns a random words from that file.

"""

import random

with open('sowpods.txt', 'r') as f:
    lines = f.readlines()
    for i in range (len(lines)):
        lines[i] = lines[i].strip()

    random_num = random.randint(0, len(lines))
    random_word = lines[random_num]
    print("You random word is", random_word)