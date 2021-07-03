
import random


stages = [
    """
    +---+
    |   |
    0   |
        |
        |
        |
    ===========
    """, """
    +---+
    |   |
    0   |
   /|   |
        |
        |
    ===========
    """, """
    +---+
    |   |
    0   |
   /|\  |
        |
        |
    ===========
    """, """
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        |
    ===========
    """, """
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        |
    ===========
    """
]

word = ["Apple", "Banana", "Orange"]

guess_word = random.choice(word).lower()

word_dash = list(guess_word)
for letter in range(len(word_dash)):
    word_dash[letter] = "_"


chance = 1
while chance != len(stages)+1:
    if "_" in word_dash:
        user_char = input("Guess a letter : ").lower()
        isChange = False
        for position in range(len(guess_word)):
            if guess_word[position] == user_char:
                word_dash[position] = user_char
                isChange = True
                continue

        if isChange is True:
            print("".join(word_dash))
        else:
            print(stages[chance-1])
            chance += 1
            if chance == len(stages)+1:
                print("you lose")
            else:
                print(f"You have {len(stages)-chance} chances left")

    else:
        print("You win")
        break
