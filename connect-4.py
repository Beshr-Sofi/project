# Program: A board of 7 columns x 6 rows is displayed, Players choose a symbol, either X or O. In their turn, they drop the symbol from top of the board (number 6) until it settles in the bottom empty cell,The first player to connect 4 symbols horizontally, vertically or diagonally wins.
# Author: Mohamed Beshr Al Sofi , 20230717
# Version:1.00
# Date: 29/2/2024


#function to display game status in each turn
def game_status(game):
    print ('|  1  |  2  |  3  |  4  |  5  |  6  |  7  |\n___________________________________________')
    for i in range(6):
        print('|  ',end='')
        for j in range(7):
            print(game[i][j], end='  |  ')
        # print('\n___________________________________________')
        print('\n')

#function to check horizontal winning case
def horizontal_check_win(game, row , column):
    if column + 1 <=6 and column + 2 <=6 and column + 3<=6:
        if game[row][column]== 'X' and game[row][column + 1]=='X' and game[row][column + 2]=='X' and game[row][column + 3]=='X':
            return True
        elif game[row][column]== 'O' and game[row][column + 1]=='O' and game[row][column + 2]=='O' and game[row][column + 3]=='O':
            return True
    if column-1 >=0 and column-2 >=0 and column-3 >=0:
        if game[row][column]=='X' and game[row][column - 1]=='X' and game[row][column - 2]=='X' and game[row][column - 3]=='X' :
            return True
        elif game[row][column]=='O' and game[row][column - 1]=='O' and game[row][column - 2]=='O' and game[row][column - 3]=='O' :
            return True
    if column+1 <=6 and column+2 <=6 and column-1 >=0:
        if game[row][column]=='X' and game[row][column + 1]=='X' and game[row][column + 2]=='X' and game[row][column - 1]=='X':
            return True
        elif game[row][column]=='O' and game[row][column + 1]=='O' and game[row][column + 2]=='O' and game[row][column - 1]=='O':
            return True
    if column-1 >=0 and column-2 >=0 and column+1<=6:
        if game[row][column]=='X' and game[row][column - 1]=='X' and game[row][column - 2]== 'X' and game[row][column + 1]=='X':
            return True
        elif game[row][column]=='O' and game[row][column - 1]=='O' and game[row][column - 2]== 'O' and game[row][column + 1]=='O':
            return True
    return False

#function to check vertical winning case
def vertical_check_win(game, row ,column):
    if row+1 <=5 and row+2 <=5 and row+3 <=5:
        if game[row][column-1] =='X' and game[row+1][column-1]=='X' and game[row+2][column-1]=='X'and game[row+3][column-1]=='X':
            return True
        elif game[row][column-1] =='O' and game[row+1][column-1]=='O' and game[row+2][column-1]=='O'and game[row+3][column-1]=='O':
            return True
    else:
        return False

#function to check diagonal winning case
def diagonal_check_win(game,row,column):
    if row+1 <=5 and row+2 <=5 and row+3 <=5 and column-1 >=0 and column-2 >=0 and column-3 >=0:
        if game[row][column]== 'X' and game[row+1][column-1]== 'X' and game[row+2][column-2]== 'X' and game[row+3][column-3]=='X':
            return True
        elif game[row][column]== 'O' and game[row+1][column-1]== 'O' and game[row+2][column-2]== 'O' and game[row+3][column-3]=='O':
            return True
    if row-1 >=0 and row-2 >=0 and row-3 >=0 and column+1 <=6 and column+2 <=6 and column+3 <=6:
        if game[row][column]== 'X' and game[row-1][column+1]=='X' and game[row-2][column+2]=='X' and game[row-3][column+3]=='X':
            return True
        elif game[row][column]== 'O' and game[row-1][column+1]=='O' and game[row-2][column+2]=='O' and game[row-3][column+3]=='O':
            return True
    if row-1 >=0 and row-2 >=0 and row+1 <=5 and column+1 <=6 and column+2 <=6 and column-1 >=0:
        if game[row][column]=='X' and game[row+1][column-1]=='X' and game[row-1][column+1]=='X' and game[row-2][column+2]=='X':
            return True
        elif game[row][column]=='O' and game[row+1][column-1]=='O' and game[row-1][column+1]=='O' and game[row-2][column+2]=='O':
            return True
    if row-1 >=0 and row+1 <=5 and row + 2 <=5 and column+1 <=6 and column-1 >=0 and column-2 >=0:
        if game[row][column]=='X' and game[row-1][column+1]=='X' and game[row+1][column-1]=='X' and game[row+2][column-2]=='X':
            return True
        elif game[row][column]=='O' and game[row-1][column+1]=='O' and game[row+1][column-1]=='O' and game[row+2][column-2]=='O':
            return True
    if row+1 <=5 and row+2 <=5 and row+3 <=5 and column+1 <=6 and column+2 <=6 and column+3 <= 6:
        if game[row][column] == 'X' and game[row + 1][column + 1] == 'X' and game[row + 2][column + 2] == 'X' and game[row + 3][column + 3] == 'X':
            return True
        elif game[row][column] == 'O' and game[row + 1][column + 1] == 'O' and game[row + 2][column + 2] == 'O' and game[row + 3][column + 3] == 'O':
            return True
    if row-1 >=0 and row-2 >=0 and row-3 >=0 and column-1 >=0 and column-2 >=0 and column-3 >= 0:
        if game[row][column]== 'X' and game[row-1][column-1]=='X' and game[row-2][column-2]=='X' and game[row-3][column-3]=='X':
            return True
        elif game[row][column]== 'O' and game[row-1][column-1]=='O' and game[row-2][column-2]=='O' and game[row-3][column-3]=='O':
            return True
    if row-1 >=0 and row-2 >=0 and row+1 <=5 and column-1 >=0 and column-2 >=0 and column+1 <=6:
        if game[row][column] == 'X' and game[row + 1][column + 1] == 'X' and game[row - 1][column - 1] == 'X' and game[row - 2][column - 2] == 'X':
            return True
        elif game[row][column] == 'O' and game[row + 1][column + 1] == 'O' and game[row - 1][column - 1] == 'O' and game[row - 2][column - 2] == 'O':
            return True
    if row-1 >=0 and row+1 <=5 and row + 2 <=5 and column-1 >=0 and column+1 <=6 and column+2 <=6:
        if game[row][column]=='X' and game[row-1][column-1]=='X' and game[row+1][column+1]=='X' and game[row+2][column+2]=='X':
            return True
        elif game[row][column]=='O' and game[row-1][column-1]=='O' and game[row+1][column+1]=='O' and game[row+2][column+2]=='O':
            return True
    return False


# welcome message and player to choose symbol and display game status
while True:
    print ("*********** Hello to Connect-4 game ***********".upper())
    p1=input("Player 1 please enter your symbol X or O: ").upper()
    while p1 != 'X' and p1 != 'O':
        p1 = input("Invalid choice\nPlease enter your symbol X or O: ").upper()
    if p1 == 'X': p2 = 'O'
    elif p1 == 'O': p2 = 'X'
    game = [['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-']]
    game_status(game)




    #take the number of place that the first player want to play and checking winning case
    row=5
    x = True
    for i in range(0,43):
        turn = p1
        column = input("First player enter place where you want to play: ")
        while not column.isdigit() or int(column) < 1 or int(column) > 7:
            column = input("Invalid please enter a correct place\nFirst player enter place where you want to play: ")
        while game[0][int(column)-1] =='X' or game[0][int(column)-1] =='O':
             column = input("This column is full\nenter in different place: ")
             while not column.isdigit() or int(column) < 1 or int(column) > 7:
                 column = input("Invalid please enter a correct place\nFirst player enter place where you want to play: ")
        column = int(column)
        row = 5
        while row >=0:
            if game[row][column - 1] == '-':
                game[row][column - 1] = turn
                break
            else:
                row -=1
        if vertical_check_win(game,row,column) or horizontal_check_win(game,row,(column-1)) or diagonal_check_win(game,row,(column-1)):
            game_status(game)
            print("<<<<player 1 is winner>>>>".upper())
            x = False
            break
        else:
            game_status(game)

        # take the number of place that the second player want to play and checking winning case
        turn=p2
        column = input("Second player enter place where you want to play: ")
        while not column.isdigit() or int(column) < 1 or int(column) > 7:
            column = input("Invalid please enter a correct place\nSecond player enter place where you want to play: ")
        while game[0][int(column) - 1] == 'X' or game[0][int(column) - 1] == 'O':
            column = input("This column is full\nenter in different place: ")
            while not column.isdigit() or int(column) < 1 or int(column) > 7:
                column = input(
                    "Invalid please enter a correct place\nSecond player enter place where you want to play: ")
        column = int(column)
        row=5
        while row >=0:
            if game[row][column - 1] == '-':
                game[row][column - 1] = turn
                break
            else:
                row-=1
        if  vertical_check_win(game,row,column) or horizontal_check_win(game,row,(column-1)) or diagonal_check_win(game,row,(column-1)):
            game_status(game)
            print("<<<<player 2 is winner>>>>".upper())
            x = False
            break
        else:
            game_status(game)


    #show draw case
    if(x):
        print("Draw")

    #ask the player if he want to play again
    restart_game =input("Do you want to play again? ").lower()
    while restart_game !='yes' and restart_game !='no':
        restart_game= input('Invalid\nPlease enter yes or no: ').lower()

    if restart_game == 'yes':
        continue
    elif restart_game == 'no':
        print('thanks for playing'.upper())
        break