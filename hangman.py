# Imports
import random, words, visual_hangman

# Initialisation
game_over = False # Initialise game as continuing
guesses = [] # Array for visual of word being guessed
remaining_guesses = 7 # Update to number of hangman visuals
game_words = words.game_words # Game words from word file

Word = game_words[random.randint(0, len(game_words)-1)].upper()

# Print function
def remaining_visuals():
    if remaining_guesses == 0:
        print(visual_hangman.display_visual_hangman[7])
    elif remaining_guesses == 1:
        print(visual_hangman.display_visual_hangman[6])
    elif remaining_guesses == 2:
        print(visual_hangman.display_visual_hangman[5])
    elif remaining_guesses == 3:
        print(visual_hangman.display_visual_hangman[4])
    elif remaining_guesses == 4:
        print(visual_hangman.display_visual_hangman[3])
    elif remaining_guesses == 5:
        print(visual_hangman.display_visual_hangman[2])
    elif remaining_guesses == 6:
        print(visual_hangman.display_visual_hangman[1])
    elif remaining_guesses == 7:
        print(visual_hangman.display_visual_hangman[0])

# display current word
    print("\n Word: ")
    for letter in guesses: # Display hidden word visual
        print(f"{letter} ", end="")
        print(f" \n {remaining_guesses} left \n")


# Create hidden word
for i in range(len(Word)):
    guesses.append('_')

# Game
while game_over == False:
    remaining_visuals()

    userInput = input("Enter letter: ")

    if not userInput:
        print("invalid input")
    else:
        if (): # Correct guess
            continue
        else: # Incorrect guess
            print("guess is incorrect")
            remaining_guesses -= 1
            # Game over case
            if remaining_guesses == 0:
                game_over = True # Exit game



# End conditions
    # Lose

    # Win

