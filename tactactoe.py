def gridView():
    """ this function use to print grid"""
    print('-' * 12)
    print(lst[0], "|", lst[1], '|', lst[2], '|')
    print(lst[3], "|", lst[4], '|', lst[5], '|')
    print(lst[6], "|", lst[7], '|', lst[8], '|')
    print('-' * 12)

def checkChoice(choice1):
    """ This function use to check if entered position is empty or not and return 0 if filled """
    for i in range(10):
        if i == choice1:
            if lst[i - 1] == 'X':
                return 0
            elif lst[i - 1] == 'O':
                return 0
            else:
                return 1

def checks():
    """This function use to check the winning positions"""
    result = 0
    # Vertical checks
    if (lst[0] == 'X' and lst[1] == 'X' and lst[2] == 'X') or (lst[0] == 'O' and lst[1] == 'O' and lst[2] == 'O'):
        result = 1
    elif (lst[3] == 'X' and lst[4] == 'X' and lst[5] == 'X') or (lst[3] == 'O' and lst[4] == 'O' and lst[5] == 'O'):
        result = 1
    elif (lst[6] == 'X' and lst[7] == 'X' and lst[8] == 'X') or (lst[6] == 'O' and lst[7] == 'O' and lst[8] == 'O'):
        result = 1
    # Horizontal checks
    if (lst[0] == 'X' and lst[3] == 'X' and lst[6] == 'X') or (lst[0] == 'O' and lst[3] == 'O' and lst[6] == 'O'):
        result = 1
    elif (lst[1] == 'X' and lst[4] == 'X' and lst[7] == 'X') or (lst[1] == 'O' and lst[4] == 'O' and lst[7] == 'O'):
        result = 1
    elif (lst[2] == 'X' and lst[5] == 'X' and lst[8] == 'X') or (lst[2] == 'O' and lst[5] == 'O' and lst[8] == 'O'):
        result = 1
    # diagonal
    if (lst[0] == 'X' and lst[4] == 'X' and lst[8] == 'X') or (lst[0] == 'O' and lst[4] == 'O' and lst[8] == 'O'):
        result = 1
    elif (lst[2] == 'X' and lst[4] == 'X' and lst[6] == 'X') or (lst[2] == 'O' and lst[4] == 'O' and lst[6] == 'O'):
        result = 1
    return result


y = 1
while y == 1:
    print("TIC TAC TOE GAME".center(50))
    print('-' * 50)
    player1 = input("Enter Player1 Name: ")
    player2 = input("Enter Player2 Name: ")
    print("Player 1 name is {} and your symbol is X\nPlayer 2 name is {} and your symbol is 0".format(player1, player2))
    print('-' * 50)
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gridView()
    c1 = 1
    c2 = 0
    for a in range(1, 10):
        if c1 == 1:
            choice = input('{}\'s turn, Please enter your position: '.format(player1))
            choice = int(choice)
            cc = checkChoice(choice)

            while cc != 1:
                if cc == 0:
                    choice = input(
                        '{} this position is already filled, Please enter another position: '.format(player1))
                    choice = int(choice)
                    cc = checkChoice(choice)

            if cc == 1:
                for i in range(10):
                    if i == choice:
                        lst[i - 1] = 'X'
            gridView()

            # to check the winner
            chk1 = checks()
            if chk1 == 1:
                print(player1 + " Win this Game")
                break
            c1 = 0
            c2 = 1
        elif c2 == 1:
            choice = input('{} \' turn, Please enter your position: '.format(player2))
            choice = int(choice)
            cc = checkChoice(choice)

            while cc != 1:
                if cc == 0:
                    choice = input(
                        '{} this position is already filled, Please enter another position: '.format(player2))
                    choice = int(choice)
                    cc = checkChoice(choice)
            if cc == 1:
                for i in range(10):
                    if i == choice:
                        lst[i - 1] = 'O'
            gridView()
            # to check the winner
            chk1 = checks()
            if chk1 == 1:
                print(player2 + " Win this Game")
                break
            c2 = 0
            c1 = 1
    finals = input("Game end\nIf you want to continue press 1 or press any key to exit")
    y = int(finals)
