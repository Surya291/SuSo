import numpy as np




def check_in_row(sud, r, num):
    for c in range(0, 9):
        if (sud[r][c] == num):
            return True
    return False


def check_in_col(sud, c, num):
    for r in range(0, 9):
        if (sud[r][c] == num):
            return True
    return False


def check_in_grid(sud, r, c, num):
    row = r - (r % 3)
    col = c - (c % 3)
    for a in range(row, row + 3):
        for b in range(col, col + 3):
            if (sud[a][b] == num):
                return True
    return False


def is_safe(sud, r, c, num):
    return (not (check_in_grid(sud, r, c, num)) and (not (check_in_row(sud, r, num))) and (
        not (check_in_col(sud, c, num))))

maze=np.array([[5,0,0, 1,0,4, 0,0,6],
          [6,0,4, 4,4,2, 0,0,7],
          [0,7,0, 0,3,0, 0,2,0],

          [0,0,4, 0,8,0, 3,0,0],
          [3,0,0, 0,0,0, 0,0,9],
          [0,0,0, 3,0,1, 0,0,0],

          [0,0,7, 0,1,8, 5,0,0],
          [9,5,0, 7,0,8, 0,4,2],
          [0,0,0, 0,0,0, 0,0,0]])

def valid_sud(maze):
    same = []
    for r in range(0, 9):
        for c in range(0, 9):
            if (maze[r][c] != 0):

                temp = maze[r][c]
                maze[r][c] = 0
                if (not is_safe(maze, r, c, temp)):
                    print("INVALID SUDOKU -- > (row,col) :: ", (r, c))
                    same.append((r,c))
                maze[r][c] = temp
    return same

same = valid_sud(maze)
print(same)
print(len(same))



