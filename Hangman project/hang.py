import random
# word_list = ["monkey", "tiger", "camel", "baboon"]
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

# print(f"Pass the solution {chosen_word}")


display = []

for _ in range(word_length):
    display += "_"
# print(display)



from hangman_art import logo, stages

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter:{guess}")
        if letter == guess:
            display[position] = letter
        #else:
            # print("No match")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])