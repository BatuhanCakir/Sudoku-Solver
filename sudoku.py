
import time
#checks if the number m is acceptable at the given row
def find_row(row, m, board):
    for n in range(9):
        if board[row][n] == m:
            return False
    return True
#checks if the number is acceptable at the given column
def find_col(col,m,board):
    for n in range(9):
        if board[n][col] == m:
            return False
    return True
#checks if the number is acceptable in the box
def check_box2(i,j,n,board):
    i_start = int(i / 3) * 3
    j_start = int(j / 3) * 3

    lst_box = []
    for i in range(3):
        for j in range(3):
            lst_box.append(board[i_start+i][j_start+j])
    for m in range(9):
        if(lst_box[m]== n):
            return False
    return True

def check_all(row,col,n,board):
    return check_box2(row,col,n,board) and find_col(col,n,board) and find_row(row,n,board)
#finds the next zero cell
def find_next_zero_cell(l,board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False
#iterates through the empty cells
def check_new(board):
    l = [0, 0]
    #when true then the sudoku is solved
    if not find_next_zero_cell(l,board):
       return True
    i = l[0]
    j = l[1]
    for n in range(1,10):
        if check_all(i,j,n,board):
            board[i][j]=n
            if check_new(board):
                return True
            board[i][j] = 0
    return False
#print the board
def show(board):
    for i in range(9):
        print(board[i])

start_time = time.time()
if __name__ == "__main__":


    grid = [[0 for x in range(9)] for y in range(9)]

    # assigning values to the grid
    grid=[[8,0,0,0,0,0,0,0,0],
       [0,0,3,6,0,0,0,0,0],
       [0,7,0,0,9,0,2,0,0],
       [0,5,0,0,0,7,0,0,0],
       [0,0,0,0,4,5,7,0,0],
       [0,0,0,1,0,0,0,3,0],
       [0,0,1,0,0,0,0,6,8],
       [0,0,8,5,0,0,0,1,0],
       [0,9,0,0,0,0,4,0,0]]


    if (check_new(grid)):
        show(grid)
    else:
        print("No solution exists")

#prints the length
print (time.time() - start_time, 's')



