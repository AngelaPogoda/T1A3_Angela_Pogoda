# Imports
import words, visual_hangman

# Initialisation
game_over = False #initialise game as continuing
guesses = [] # Array for visual of word being guessed
incorrect_guesses = 0 
remaining_guesses = 7 #update to number of hangman images
game_words = words.game_words # game words from word file

# print function
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

# game
while game_over == False:
    remaining_visuals()

    userInput = input("Enter letter: ")

    if not userInput:
        print("invalid input")
    else:
        if (): # correct guess
            continue
        else: # incorrect guess
            remaining_guesses -= 1
            # game over case
            if remaining_guesses == 0:
                game_over = True



# end conditions
    # Lose

    # Win

