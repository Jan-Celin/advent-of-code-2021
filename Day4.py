nums = input().split(',')

boards = []
while True:
    praz = input()
    red = input()
    if red == 'END':
        break
    
    board = []
    board.append(red.split())
    for i in range(4):
        red = input()
        board.append(red.split())

    boards.append(board)




for i in nums:
    for j, board in enumerate(boards):
        bingo = 0
        rem_boards = []
        for k, row in enumerate(board):
            for l, element in enumerate(row):
                if element == i:
                    boards[j][k][l] = -1
                    
##                    bingo = 1
##                    for x in range(5):
##                        if boards[j][x][l] != -1:
##                            bingo = 0
##                            break
##                    if bingo == 1:
##                        rem_boards.append(board)
##                        for test1 in boards: ##
##                            for test2 in test1:
##                                print(test2)
##                            print("\n")
##                        print('--', board)
##                        print("\n")
##                        break
##
##                    bingo = 1
##                    for x in range(5):
##                        if row[x] != -1:
##                            bingo = 0
##                            break
##                    if bingo == 1:
##                        rem_boards.append(board)
##                        for test1 in boards: ##
##                            for test2 in test1:
##                                print(test2)
##                            print("\n")
##                        print('--', board)
##                        print("\n")
##                        break
##                    
##            if bingo == 1:
##                break
##            
##        if bingo == 1:
##            bingo = 0
##            continue
##    for b in rem_boards:
##        print(1)
##        boards.remove(b)

    remboards = []
    for j, board in enumerate(boards):
        rem_boards = []
        for k, row in enumerate(board):
            bingo = 1
            for l, element in enumerate(row):
                if element != -1:
                    bingo = 0
                    break
            if bingo == 1:
                if board not in remboards:
                    remboards.append(board)
                break

        for l in range(5):
            bingo = 1
            for m in range(5):
                if board[m][l] != -1:
                    bingo = 0
                    break
            if bingo == 1:
                if board not in remboards:
                    remboards.append(board)
                break

    for j in remboards:
        boards.remove(j)
        
    if len(boards) == 1:
        winnum = i
        break

for i in boards[0]:
    print(i)
print(winnum)












