def clean(testcase):
    temp = testcase.replace('.','0')
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(temp[(9*i)+j])
        board.append(row)
    new_list = [[int(x) for x in lst] for lst in board]
    return new_list

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
 
def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  
def check_location_is_safe(arr,row,col,num): 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 
  
def solve_sudoku(arr):     
    l=[0,0]     
    if(not find_empty_location(arr,l)): 
        return True
    row=l[0] 
    col=l[1] 
    for num in range(1,10): 
        if(check_location_is_safe(arr,row,col,num)): 
            arr[row][col]=num 
            if(solve_sudoku(arr)): 
                return True
            arr[row][col] = 0       
    return False  

def main(testcase):
    board = clean(testcase)
    solve_sudoku(board)
    #print_board(board) 

# t ='..5..8..18......9.......78....4.....64....9......53..2.6.........138..5....9.714.'
# main(t)