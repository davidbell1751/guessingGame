# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
try:
 # list of variables
    middle_name = "kelly"
    guess = str
    guess_count = 0                        # how many times the user has guessed
    guess_limit = 3                        # how many guesses are available
    out_of_names = False                  # boolean to let us know if the user is out of guesses



    while guess != middle_name and not out_of_names:         # while condition is true as long as word is not guessed and have guesses left

        if guess_count < guess_limit:           # if guess count is less then guess limit they have more guesses to run
            guess = str(input("Enter name: "))      # the input has been set to accept a string only
            guess_count += 1                # this will add 1 to each guess count // increment the guess count by 1
            guesses_left = guess_limit - guess_count

            # print("you have ", guesses_left ," guesses left")



        else:                               # if they are out of guesses they can no longer loop and the game is over
            out_of_names = True


    if out_of_names:      # if user is out of guess then do this
        print("Out of Guesses, Come on Kelly do Better!!!")
    else:
        print("Our Little Girls full name is: Reese Kelly Bell!!")



except:
    print("Invalid Input")


