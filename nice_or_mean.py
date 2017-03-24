# Python:   2.7.13
#
#Authors:   Daniel A. Christie, Nash N. Wood
#
#Purpose:   The Tech Academy - Python Course, Item 35 "Nice or Mean"
#           Demonstrating how to pass variables from function to function
#           While producing a functional game.
#
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable to
#           the calling function.




def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game (name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):
    '''
        Check if this is a new game or not,
        if it is new, get the user's name.
        If it si not a new game, thank the player for
        playing again and continue with the game.
    '''
    if name != "": #Meaning, if we do not already have this user's name, then they are a new player and we need to gwet their name
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people.")
                    print("You can be nice or mean when interacting with them.")
                    print("At the end of the game your fate will be decided from your actions.")
                    stop = False
    return name        



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        pick = raw_input("\nA canvasser approaches you for a conversation.\nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("\nThey smile, and dive into their practiced speech...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nYou avoid eye contact and pretend to be on your phone.")
            mean = (mean + 1)
            stop = False
    show_score(nice,mean,name) # Pass the 3 variables to the score()
    nice_mean2(nice,mean,name) # Call the next function with our passed variables



def nice_mean2(nice,mean,name):
    stop = True
    while stop:
        pick = raw_input("\nYou encounter an old lady carrying groceries.\nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("\nYou help her across the street.\nShe rewards your kindness with a $5 bill.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe elderly woman angrily shakes her cane at you and says, 'Kids these days!'")
            mean = (mean + 1)
            stop = False
    show_score(nice,mean,name) # Pass the 3 variables to the score()
    nice_mean3(nice,mean,name) # Call the next function with our passed variables



def nice_mean3(nice,mean,name):
    stop = True
    while stop:
        pick = raw_input("\nYou see a baby holding candy.\nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("\nYou smile at the tiny human and carry on with your stroll.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nYou swiftly take the candy and hold no remorse in your heart.")
            mean = (mean + 1)
            stop = False
    show_score(nice,mean,name) # Pass the 3 variables to the score()
    nice_mean4(nice,mean,name) # Call the next function with our passed variables



def nice_mean4(nice,mean,name):
    stop = True
    while stop:
        pick = raw_input("\nYou encounter a homeless man asking for change.\nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("\nYou hand the disheveled man a few quarters.  He grins a toothless grin.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nYou tell the man to 'Get a job!'")
            mean = (mean + 1)
            stop = False
    show_score(nice,mean,name) # Pass the 3 variables to the score()
    nice_mean5(nice,mean,name) # Call the next function with our passed variables



def nice_mean5(nice,mean,name):
    stop = True
    while stop:
        if nice == 4:
            score(nice,mean,name)
        if mean == 4:
            score(nice,mean,name)
        else:
            pick = raw_input("\nYou spot a squirrel 20 yards in front of your car.\nWill you be nice or mean? n/m:").lower()
            if pick == "n":
                print("You narrowly miss the fluffy creature and continue on your way.")
                nice = (nice + 1)
                stop = False
            if pick == "m":
                print("\nThe soft thud slides a tight smile across your lips.")
                mean = (mean + 1)
                stop = False
    show_score(nice,mean,name) # Pass the 3 variables to the score()
    score(nice,mean,name) #tally the score    



def show_score(nice,mean,name):
    print("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))

def score(nice,mean,name):
        # Score function is being passed the values stored within the 3 variables
        if nice >= 4: # if condition is valid, call win function passing in the variables so it can use them
            win(nice,mean,name)
        if mean >= 4: # if condition is valid, call loss function passing in the variables so it can use them
            lose(nice,mean,name)
        else:        #  else, call nice_mean function passing in the variables so it can use them
            nice_mean(nice,mean,name)



def win(nice,mean,name):
    print("\nNice job {}, you have won! \nEveryone loves you and you really are a nice person!".format(name)) # Gives the wildcard our name variable
    again(nice,mean,name) # Call again function and pass in our variables



def lose(nice,mean,name):
    print("\nI'm dissapointed in you {}, you have lost! \nHow could you be so mean?".format(name)) # Gives the wildcard our name variable
    again(nice,mean,name) # Call the again function and pass in our variables



def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee you soon!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for YES or 'n' for NO.")


                             
def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, we do not need to reset the name variable if the same user wants to play again
    start(nice,mean,name)


        
if __name__ == "__main__":
    start()
