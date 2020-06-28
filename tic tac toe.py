Options = []

for x in range (0, 9) :
    Options.append(str(x + 1))
Player= True
winner = False

def printBoard() :
    print( '\n -----')
    print( '|' + Options[0] + '|' + Options[1] + '|' + Options[2] + '|')
    print( ' -----')
    print( '|' + Options[3] + '|' + Options[4] + '|' + Options[5] + '|')
    print( ' -----')
    print( '|' + Options[6] + '|' + Options[7] + '|' + Options[8] + '|')
    print( ' -----\n')
count=0

while not winner :

    printBoard()
    
    if(count>=9):
        print("Draw")
        break
    if Player :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("Please enter a valid field")
        continue
    if(choice>9):
        break
    if Options[choice - 1] == 'X' or Options [choice-1] == 'O':
        print("Invalid move, plase try again")
        continue

    if Player :
        count+=1
        Options[choice - 1] = 'X'
    else :
        count+=1
        Options[choice - 1] = 'O'

    Player = not Player

    for x in range (0, 3) :
        y = x * 3
        if (Options[y] == Options[(y + 1)] and Options[y] == Options[(y + 2)]) :
            winner = True
            printBoard()
        if (Options[x] == Options[(x + 3)] and Options[x] == Options[(x + 6)]) :
            winner = True
            printBoard()

    if((Options[0] == Options[4] and Options[0] == Options[8]) or 
       (Options[2] == Options[4] and Options[4] == Options[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(Player + 1)) + " wins!\n")
