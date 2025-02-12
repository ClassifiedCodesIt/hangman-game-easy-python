
from hangman_art import logo_welcome 
from hangman_art import logo_dead
from hangman_art import logo_win
from hangman_words import word_list
import random
print(logo_welcome)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}.")
            print(logo_dead)
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(logo_win)
    from hangman_art import stages
    print(stages[lives])
    