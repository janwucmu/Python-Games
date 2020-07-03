theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def instruction():
    print("press the numbers to place your X or O in position\n")    
    print('  ', '1', '  |','  ' ,'2', '  |', '  ','3')
    print('-------+--------+--------')
    print('  ', '4', '  |','  ' ,'5', '  |', '  ','6')
    print('-------+--------+--------')
    print('  ', '7', '  |','  ' ,'8', '  |', '  ','9', '\n')
    print('=========================\n')

def display_board():    
    print('  ', theBoard['1'], '  |','  ' ,theBoard['2'], '  |', '  ',theBoard['3'])
    print('-------+--------+--------')
    print('  ', theBoard['4'], '  |','  ' ,theBoard['5'], '  |', '  ',theBoard['6'])
    print('-------+--------+--------')
    print('  ', theBoard['7'], '  |','  ' ,theBoard['8'], '  |', '  ',theBoard['9'], '\n')

def check_winner():
    check = False
    if ((theBoard['7'] == 'X' and theBoard['8'] == 'X' and theBoard['9'] == 'X') or 
        (theBoard['7'] == 'O' and theBoard['8'] == 'O' and theBoard['9'] == 'O')):
        check = True
    elif ((theBoard['7'] == 'X' and theBoard['4'] == 'X' and theBoard['1'] == 'X') or
        (theBoard['7'] == 'O' and theBoard['4'] == 'O' and theBoard['1'] == 'O')):
        check = True
    elif ((theBoard['7'] == 'X' and theBoard['5'] == 'X' and theBoard['3'] == 'X') or
        (theBoard['7'] == 'O' and theBoard['5'] == 'O' and theBoard['3'] == 'O')) :
        check = True
    elif ((theBoard['4'] == 'X' and theBoard['5'] == 'X' and theBoard['6'] == 'X') or 
        (theBoard['4'] == 'O' and theBoard['5'] == 'O' and theBoard['6'] == 'O')):
        check = True
    elif ((theBoard['1'] == 'X' and theBoard['2'] == 'X' and theBoard['3'] == 'X') or
        (theBoard['1'] == 'O' and theBoard['2'] == 'O' and theBoard['3'] == 'O')):
        check = True
    elif ((theBoard['1'] == 'X' and theBoard['5'] == 'X' and theBoard['9'] == 'X') or
        (theBoard['1'] == 'O' and theBoard['5'] == 'O' and theBoard['9'] == 'O')):
        check = True
    elif ((theBoard['9'] == 'X' and theBoard['6'] == 'X' and theBoard['3'] == 'X') or
        (theBoard['9'] == 'O' and theBoard['6'] == 'O' and theBoard['3'] == 'O')):
        check = True
    elif ((theBoard['2'] == 'X' and theBoard['5'] == 'X' and theBoard['8'] == 'X') or
        (theBoard['2'] == 'O' and theBoard['5'] == 'O' and theBoard['8'] == 'O')):
        check = True
    return check

def play():
    node = "O"
    check = False
    for i in range(9):
        instruction()
        display_board()
        print('it is ', node, 'turn to play \n')
        turn = input("pick a empty box with numbers from 1-9: ")
        while True:
            if theBoard[turn] == ' ':
                theBoard[turn] = node
                break
            else:
                print("you've already played that move, place your", node, "elsewhere\n")
                instruction()
                display_board()
                turn = input("pick a empty box with numbers from 1-9: ")
        check = check_winner()
        if check == True:
            print('The winner is', node)
            break
        if node == 'X':
            node = 'O'
        else:
            node = 'X'
    if not check: 
        print("No winner")

play()
display_board() 