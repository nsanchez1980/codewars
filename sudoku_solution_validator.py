def valid_solution(board):
    index = 0
    lil_column = []
    lil_row = []
    lil_board = []
    for row in board:
        for y in row:
            if y==0:
                return False
            if row.count(y)!=1:
                return False
    while index < 9:
        for row in board:
            lil_column.append(row[index])
        print(lil_column)
        for y in lil_column:
            if lil_column.count(y)!=1:
                return False
        lil_column.clear()
        index = index + 1
    index = 0
    index_to = 3
    offset = 0
    offset_to = 3
    while offset_to<=9:
        while index_to<=9:
            while offset<offset_to:
                while index<index_to:
                    lil_board.append(board[offset][index])
                    index = index + 1
                offset = offset + 1
                index = 0
            for x in lil_board:
                if lil_board.count(x)!=1:
                    return False
            lil_board = []
            index = index + 3
            index_to = index_to + 3
        index_to = 3
        offset_to = offset_to + 3
    return True

    
            



print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);