def guessing_game():
    print("Guess the number from 0 to 1000 and I will guess it in 10 guesses or less!")
    #minimum and maximum set the range of the game
    minimum = 0
    maximum = 1000
    #check_list is a list, that will change its length as the game goes on, the first "if" will monitor its length in
    #order to avoid the game going on for ever
    check_list = list(range(minimum, maximum + 1))
    guess = int(((maximum - minimum) /2) + minimum)
    print(f"My guess is {guess}")
    #when "guessed" changes value to True, the game will end
    guessed = False
    if len(check_list) >= 1:
        while not guessed:
            reply_from_user = input("Did I guess correctly? (yes/no) ")
            #if guess is correct, end the game
            if reply_from_user.lower() == "yes":
                print("I won!")
                guessed = True
            #if guess is incorrect, proceed to ask questions
            elif reply_from_user == "no":
                reply_from_user_2 = input("Was my guess too high? (yes/no)")
                #used second boolean, in order to have the possibility to stay in the correct loop, if the answer is
                #neither yes nor no
                guessed_2 = False
                while not guessed_2:
                    if reply_from_user_2 == "yes":
                        maximum = guess
                        guess = int(((maximum - minimum) / 2) + minimum)
                        guessed_2 = True
                        print(f"My guess is {guess}")
                    elif reply_from_user_2 == "no":
                        reply_from_user_3 = input("Was my guess too low? (yes/no)")
                        #used third boolean, for the exact same reason as the second one
                        guessed_3 = False
                        while not guessed_3:
                            if reply_from_user_3 == "yes":
                                minimum = guess
                                guess = int(((maximum - minimum) / 2) + minimum)
                                guessed_3 = True
                                guessed_2 = True
                                print(f"My guess is {guess}")
                            #if the answer in not correct, too high or too low, then the user provided wrong answer
                            #somewhere, which will return the game to the first loop
                            elif reply_from_user_3 == "no":
                                print("DON'T LIE TO ME!")
                                guessed_3 = True
                                guessed_2 = True
                            elif reply_from_user_3 not in {"yes", "no"}:
                                print("Please answer yes or no")
                    elif reply_from_user_2 not in {"yes", "no"}:
                        print("Please answer yes or no")
            elif reply_from_user.lower not in {"yes", "no"}:
                print("Please answer yes or no")
    else:
        print(f"My final guess is {guess}, it should be correct unless you have lied...")



guessing_game()