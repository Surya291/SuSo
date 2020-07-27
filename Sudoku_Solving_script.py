def Suso (sud):
    k = [0,0]

    if(not unassigned(sud,k)):
        return True

    r = k[0]
    c = k[1]

    for num in range(1,10):
        if (is_safe(sud,r,c,num)):
            sud[r][c] = num

            if Suso(sud):
                return True
            sud[r][c] = 0
    return False

def unassigned(sud,k):
    for r in range(0,9):
        for c in range(0,9):
            if (sud[r][c] == 0):
                k[0] = r
                k[1] = c
                return True
    return False

def check_in_row(sud,r,num):
    for c in range(0,9):
        if(sud[r][c]== num):
            return True
    return False

def check_in_col(sud,c,num):
    for r in range(0,9):
        if(sud[r][c]== num):
            return True
    return False

def check_in_grid(sud,r,c,num):
    row = r -(r%3)
    col = c - (c%3)
    for a in range(row,row+3):
        for b in range(col,col+3):
            if(sud[a][b] == num):
                return True
    return False
def is_safe(sud,r,c,num):
    return (not(check_in_grid(sud,r,c,num))and (not(check_in_row(sud,r,num))) and (not(check_in_col(sud,c,num))))


'''
def print_grid(sud):
    for c in range(9):
        print(sud[:][c])


sud=[     [5,0,0, 1,0,4, 0,0,6],
          [6,0,0, 9,0,2, 0,0,7],
          [0,7,0, 0,3,0, 0,2,0],

          [0,0,4, 0,8,0, 3,0,0],
          [3,0,0, 0,0,0, 0,0,9],
          [0,0,0, 3,0,1, 0,0,0],

          [0,0,7, 0,1,0, 5,0,0],
          [9,5,0, 7,0,8, 0,4,2],
          [0,0,0, 0,0,0, 0,0,0]]






if(Suso(sud)):
    print_grid(sud)
else:
    print("NO SOLN")'''

'''    
    
sud=[     [0,0,0, 0,0,0, 0,0,0],
          [0,0,0, 0,0,0, 0,0,0],
          [0,0,0, 0,0,0, 0,0,0],

          [0,0,0, 0,0,0, 0,0,0],
          [0,0,0, 0,0,0, 0,0,0],
          [0,0,0, 0,0,0, 0,0,0],

          [0,0,0, 0,0,0, 0,0,0],
          [0,0,0, 0,0,0, 0,0,0],
          [0,0,0, 0,0,0, 0,0,0]]'''
