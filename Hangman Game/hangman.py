import random


word = ["Apple", "Banana", "Orange"]

random_index = 1  # random.randrange(0,3)

guess_word = word[random_index].lower()


word_count = len(guess_word)

word_dash = list(guess_word)

find_dashes = 0

chance = 5


for letter in range(len(word_dash)):
    word_dash[letter] = "_"


def fillup(position):
    if False:
        print("raghu")
        # word_dash[s] == guess_word[s]:
        # occurance = guess_word[s+1:len(guess_word)]
        # print(occurance)
        # occur_index = occurance.find(guess_word[s])
        # print(occur_index)
        # word_dash[position+occur_index+1] = guess_word[occur_index]

    else:
        for char in range(word_count):
            if char == position:
                word_dash[char] = guess_word[char]
            else:
                if word_dash[char] == "_":
                    word_dash[char] = "_"

    return ''.join(word_dash)


while chance != 0:
    for char in range(word_count):
        user_char = input("Guess a letter : ")
        char_position = guess_word.find(user_char)
        # if word_dash[char_position] == guess_word[char_position]:
        #     occurance = guess_word[char_position+1:len(guess_word)]
        #     occur_index = occurance.find(guess_word[char_position])
        #     char_position=occur_index

        if char_position != -1:
            user_guess = fillup(char_position)
            print(user_guess)
            find_dashes = user_guess.find('_')
            if find_dashes == -1:
                print("You Won")
                break
        else:
            chance -= 1
            print("You are Wrong")
            user_guess = fillup(char_position)
            print(user_guess)
            print(f"You have {chance} chance left")
    if find_dashes == -1:
        break
