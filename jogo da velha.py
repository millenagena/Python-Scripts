def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

theBoard = {'topL': '', 'topM': '', 'topR': '',
            'midL': '', 'midM': '', 'midR': '',
            'lowL': '', 'lowM': '', 'lowR': ''}

jogadorX = input('Nome do jogador que utilizará X: ')
jogadorO = input('Nome do jogador que utilizará O: ')
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
