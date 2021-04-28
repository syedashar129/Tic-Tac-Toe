

#BOARD
boardElements = []



def printBoard (board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' ',}




#GAME
def tictac():
    count = 0
    place = 'X'

    enter = (input())

    for i in range (10):
        printBoard(theBoard)
        print ("It's your turn, " + place + ", choose a spot to place.")
        enter = (input())

        if theBoard[enter] == ' ':
            print("Enter open space number to place " + place)
            theBoard[enter] = place
            count += 1
        else:
            print("That spot is taken, please choose another spot")
            continue

        theBoard[enter] = place
        if count >= 5:   #5 bc thats minimum to win for either person
            if (theBoard['7'] == theBoard ['8'] == theBoard['9'] != ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break
            elif(theBoard['4'] == theBoard ['5'] == theBoard['6']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break
            elif (theBoard['1'] == theBoard ['2'] == theBoard['3']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')     
                break       
            elif (theBoard['8'] == theBoard ['5'] == theBoard['2']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break
            elif (theBoard['7'] == theBoard ['5'] == theBoard['3']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break
            elif (theBoard['7'] == theBoard ['4'] == theBoard['1']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break
            elif (theBoard['8'] == theBoard ['5'] == theBoard['2']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break
            elif (theBoard['9'] == theBoard ['6'] == theBoard['3']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break
            elif (theBoard['9'] == theBoard ['5'] == theBoard['1']!= ' '):
                printBoard(theBoard)
                print('Game over '+place+ ' Won!')
                break

        if count == 9:
                print (" No one won. Game resulted in a tie")
                break
        if (place == 'X'):
            place = 'O'
        else:
            place = 'X'


tictac()

# so like (789, 456, 123, 852, 753, 741, 852, 963, 951) r all winning scenarios (all of em: 9 total)