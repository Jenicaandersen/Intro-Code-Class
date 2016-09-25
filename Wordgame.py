import random #imports are an external library that we will reference in our code

def get_random_word():
    words = ["pizza", "cheese", "apples"]  #lists! begins with a zero based index. Pizza is word 0
    #len(words) will tell us 3. That's the length of the list. words.append("noodles")
    #words.reverse() would print this in reverse order. 
    random_word = words[random.randint(0, len(words)-1)]# do the words-1 because of the zero place Index
    return random_word

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

        #now we import random and begin lists



     








print("Start the Game")
play_word_games()
print("End the Game")
