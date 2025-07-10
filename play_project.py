import random

animals = ["dog", "cow", "sheep", "cat", "donkey", "horse"]

score = 0


def word_game():
    for i in range(6):
        global score
        selected_word = random.choice(animals)
        user_word = input(f"Spell this word - {selected_word}:")
        if user_word == selected_word:
            print("Well done!")
            score += 1
            print(f"Your score is {score}")
        else:
            print("Sorry. Try again!")


word_game()
