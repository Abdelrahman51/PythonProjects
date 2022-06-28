# if you run this code on jupyter remove (#) from clear_output from line 3 and 9 

#from IPython.display import clear_output
import random

def display_board(board):
    
    #To Display only one version from board but only run on jupyter
    #clear_output()
    
    #The Board
    print(board[7]+ " | "+ board[8] +" | "+ board[9])
    print("----------")
    print(board[4]+ " | "+ board[5] +" | "+ board[6])
    print("----------")
    print(board[1]+ " | "+ board[2] +" | "+ board[3])


def player_input():
    
    #Variable
    choice=  ''
    
    #Player1 Choice X or O 
    while not (choice=='X' or choice == 'O'):
        choice= input("Player1: Please Choose X or O  ").upper()
    
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, choice, position):
    
    #list the board with indexing is position replacement by marker
    board[position]=choice


def win_check(board, marker):
    
    
    return ((board[1] == board[5] == board[9] == marker) or #Diagonal
    (board[3] == board[5] == board[7] == marker) or #Diagonal
    (board[1] == board[2] == board[3] == marker) or #horizontal Bottom
    (board[4] == board[5] == board[6] == marker) or #horizontal middle
    (board[7] == board[8] == board[9] == marker) or #horizontal top
    (board[1] == board[4] == board[7] == marker) or #Vertical left
    (board[2] == board[5] == board[8] == marker) or #Vertical middle
    (board[3] == board[6] == board[9] == marker)) #Vertical Right


def choose_first():
    
    #Variable to chosse randomly who play the first
    theFirst = random.randint(0, 1)
    
    if  theFirst == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    
    #To Check if that place is empty or not
    return board[position] == ' '


def full_board_check(board):
    
    #To Check if all location is full or not 
    for i in range(1,10):
        if space_check(board, i):
            return False
        
    #That means the board is full 
    return True


def player_choice(board):
    
    #Variables
    position = 0
    
    #To check if the player choose right place and see if that space available to play in it or not
    while position not in list(range(1,10)) or not space_check(board, position):
        position = int(input("Kindly'Choose your next position: (1-9) "))
        
    return position


def replay():
        
    return input('Do you want to play again? Enter Yes or No: ')

print('############# Welcome to my Tic Tac Toe! #############')


#Start the game 
while True:
    
    # The initial board
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        
        #Player 1 Turn
        if turn == 'Player 1':
            
            #Show the board
            display_board(the_board)
            
            #Choose a position
            position = player_choice(the_board)
            
            #Replace by palyer1 marker
            place_marker(the_board, player1_marker, position)

            #Check if palyer1 is win
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            
            #Check if they tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                    
                #No Winner or no tie , the next player turn
                else:
                    turn = 'Player 2'

        else:    
        
        # Player2's turn.
                     
            #Show the board
            display_board(the_board)
            
            #Choose a position
            position = player_choice(the_board)
            
            #Replace by palyer2 marker
            place_marker(the_board, player2_marker, position)

            #Check if palyer2 is win
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won the game!')
                game_on = False
                
            #Check if they tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    game_on = False
                    
                #No Winner or no tie , the next player turn    
                else:
                    turn = 'Player 1'

    if not replay():
        break

