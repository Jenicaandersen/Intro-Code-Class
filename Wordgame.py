def get_random_word():
    return "pizza"

def play_word_games():
    strikes = 0
    max_strikes = 3 #this is creating variables
    playing = True #boolean
    #now we're going to create a loop to allow us to keep playing

    word  = get_random_word() #defining new function needs paranthesis, then I went up and defined this get_random_word

    while playing:  #this means it will continue running while this is true. Might also say while strikes < 3
        strikes += 1 #taking strikes and and setting it equal to strikes + 1

        if strikes >= max_strikes:
            playing = False
    #now our indent returns to the while place, so that we know where we're ending the while loop
    if strikes >= max_strikes:
        print("Sorry. Game Over.")
    else:
        print("Winner!") #ran and tested the code here. Good habit to keep testing



     








print("Start the Game")
play_word_games()
print("End the Game")
