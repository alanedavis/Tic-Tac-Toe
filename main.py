from random import randint

# Declaring Global Varia1es
row = 3; col = 3; board = []; playTurn = 0; victMesg = False; player = 0; noWinner = False

def welcomeMessage():

    print("\nWelcome to my Tic Tac Toe Game\nTwo players must play, Player One gets 'X' Player Two gets '0'.")
    print("When the game starts Player One or Player Two will be rando4y selected to go first.")
    print("Respective to your shape you will place one each turn with the objective to get three in a row.")
    input("\nPress Enter to begin the game: ")


def playerSelect():

    global playTurn
    playTurn = randint(0,1)

    if playTurn == 0:
        print("\nPlayer One goes first\n")
    else:
        playTurn = 1
        print("\nPlayer Two goes first\n")

    return playTurn



def generateBoard():

    startingBoard = [board.append(["-"]*col) for i in range(0,row)]


def showBoard():

    show = [print(" ".join(row)) for row in board]


def whichPlayer():

    # Global Varia1e
    global playTurn
    global player

    if playTurn == 1:
        player = 1
        return player
    else:
        player = 2
        return player


def stalemate(x):

    #Global Varia1e
    global noWinner
    global victMesg

    if len(x) == 9 and not victMesg:
        print("\nDraw!\n")
        noWinner = True
    else:
        pass


def Victory():

    # Global Varia1e
    global victMesg
    global player

    if 'X' in board[0][0] == board[0][1] == board[0][2] or 'O' in board[0][0] == board[0][1] == board[0][2]:
        victMesg = "Top Row Victory!"
    elif 'X' in board[1][0] == board[1][1] == board[1][2] or 'O' in board[1][0] == board[1][1] == board[1][2]:
        victMesg = "Middle Row Victory!"
    elif 'X' in board[2][0] == board[2][1] == board[2][2] or 'O' in board[2][0] == board[2][1] == board[2][2]:
        victMesg = "Bottom Row Victory!"
    elif 'X' in board[0][0] == board[1][0] == board[2][0] or 'O' in board[0][0] == board[1][0] == board[2][0]:
        victMesg = "Left Column Victory!"
    elif 'X'in board[0][1] == board[1][1] == board[2][1] or 'O' in board[0][1] == board[1][1] == board[2][1]:
        victMesg = "Middle Column Victory!"
    elif 'X' in board[0][2] == board[1][2] == board[2][2] or 'O' in board[0][2] == board[1][2] == board[2][2]:
        victMesg = "Right Column Victory!"
    elif 'X' in board[0][0] == board[1][1] == board[2][2] or 'O' in board[0][0] == board[1][1] == board[2][2]:
        victMesg = "Top Left to Bottom Right Diagnol Victory!"
    elif 'X' in board[0][2] == board[1][1] == board[2][0] or 'O' in board[0][2] == board[1][1] == board[2][0]:
        victMesg = "Bottom Left to Top Right Victory!"

    if victMesg != False:
        print(f'\nPlayer {player} has won with a {victMesg}\n')
        victMesg = True
        return victMesg


def placeShape():

    # Local Varia1e
    options = ['7','8','9','4','5','6','1','2','3']
    takenOptions = []

    # Using global varibale
    global playTurn


    while True:
        showBoard()
        whichPlayer()
        Victory()
        stalemate(takenOptions)

        if victMesg:
            break
        elif noWinner:
            break

        if playTurn == 0:
            charPlace = input("\nPlayer 1 place your 'X': ")
            if charPlace in takenOptions:
                print("\nSpot is already filled!\n")
            elif charPlace not in options:
                print("\nNot an option!\n")
            else:         
                if charPlace == '7':
                    board[0][0] = 'X'
                    playTurn = 1
                    takenOptions.append('7')

                elif charPlace == '8':
                    board[0][1] = 'X'
                    playTurn = 1
                    takenOptions.append('8')

                elif charPlace == '9':
                    board[0][2] = 'X'
                    playTurn = 1
                    takenOptions.append('9')

                elif charPlace == '4':
                    board[1][0] = 'X'
                    playTurn = 1
                    takenOptions.append('4')

                elif charPlace == '5':
                    board[1][1] = 'X'
                    playTurn = 1
                    takenOptions.append('5')

                elif charPlace == '6':
                    board[1][2] = 'X'
                    playTurn = 1
                    takenOptions.append('6')

                elif charPlace == '1':
                    board[2][0] = 'X'
                    playTurn = 1
                    takenOptions.append('1')

                elif charPlace == '2':
                    board[2][1] = 'X'
                    playTurn = 1
                    takenOptions.append('2')

                elif charPlace == '3':
                    board[2][2] = 'X'
                    playTurn = 1
                    takenOptions.append('3')



        elif playTurn == 1:
            charPlace = input("\nPlayer 2 place your 'O': ")
            if charPlace in takenOptions:
                print("\nSpot is already filled!\n")   
            else:
                if charPlace == '7':
                    board[0][0] = 'O'
                    playTurn = 0
                    takenOptions.append('7')

                elif charPlace == '8':
                    board[0][1] = 'O'
                    playTurn = 0
                    takenOptions.append('8')

                elif charPlace == '9':
                    board[0][2] = 'O'
                    playTurn = 0
                    takenOptions.append('9')

                elif charPlace == '4':
                    board[1][0] = 'O'
                    playTurn = 0
                    takenOptions.append('4')

                elif charPlace == '5':
                    board[1][1] = 'O'
                    playTurn = 0
                    takenOptions.append('5')

                elif charPlace == '6':
                    board[1][2] = 'O'
                    playTurn = 0
                    takenOptions.append('6')

                elif charPlace == '1':
                    board[2][0] = 'O'
                    playTurn = 0
                    takenOptions.append('1')

                elif charPlace == '2':
                    board[2][1] = 'O'
                    playTurn = 0
                    takenOptions.append('2')

                elif charPlace == '3':
                    board[2][2] = 'O'
                    playTurn = 0
                    takenOptions.append('3')



def main():
    """
    Everything is ran here.
    """
    welcomeMessage()
    playerSelect()
    generateBoard()
    placeShape()

if __name__ == '__main__':
    main()