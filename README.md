Number-guessing-game-2
the program will guess user's number
The minimum and maximum values will set the range of the game, 0-1000 by default.

check_list is a list, that will change its length as the game goes on, the first "if" will monitor its 
length in order to avoid the game going on forever.
when "guessed" changes value to True, the game will end.
The program is based on Binary search algorithm. If the range is from 0 to 1000 the first guess will be 500, which is 
the middle of the range. The user will have to provide truthful answers if the value provided by the program is correct,
too high or too low. If the answer to all three questions is "no", the loop will reset, since this set of replies is 
incorrect.
