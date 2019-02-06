from __future__ import print_function
print ("welcome to my atari adventure game! the directions to move in are defined as left, right, up, and down. Enjoy.")

x = 6
y = -2

#move = str(input('Make your move! Type in either "Left", "Right", "Up", "Down" or type "Exit" to exit the game:')).lower()

def game():
    global x
    global y
    move = str(input('Make your move! Type in either "Left", "Right", "Up", "Down" or type "Exit" to exit the game:')).lower()
    if move == ('left'):
        x = x-3
        print ('your x position is', x, '.' 'your y position is', y, '.')
        game()
    elif move == ('up'):      
        y = y+3
        print ('your x position is', x, '.' 'your y position is', y, '.')
        game()
    elif move == ('right'):
        x = x+2
        print ('your x position is', x, '.' 'your y position is', y, '.')
        game()
    elif move == ('down'):
        y = y-2
        print ('your x position is', x, '.' 'your y position is', y, '.')
        game()
    elif move == ('exit'):
        exit()
    else:
        print ("Oops!!! You have entered a wrong input, please enter either up, down, left, right or exit only.")
        game()
game()