# import time
#cleans the input testcase
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
#finds an empty square and assigns the row and column to l
def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  
#checks whether any assigned number in the specified row matches the given number
def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
#checks whether any assigned number in the specified column matches the given number
def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
#checks whether any assigned entry within the specified 3x3 box matches the given number 
def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False

#check if num is not already placed in current row,current col and current 3x3 box 
def check_location_is_safe(arr,row,col,num):  
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 
  
#sudoku solving
def solve_sudoku(arr):     
    l=[0,0] 
    # if no empty location, done   
    if(not find_empty_location(arr,l)): 
        return True
    #assigning list values to row and col from above function
    row=l[0] 
    col=l[1] 
    #checking a digit
    for num in range(1,10): 
        if(check_location_is_safe(arr,row,col,num)):  
            arr[row][col]=num
            # return true if success
            if(solve_sudoku(arr)): 
                return True
            # failure, unmake and try again 
            arr[row][col] = 0
              
    #backtracking         
    return False  


def main(testcase):
    # testcase = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    # bt_time = 0.0
    # start = time.time()
    board = clean(testcase)
    solve_sudoku(board)
    # end = time.time()
    # bt_time += (end-start)
    # print("Total time [bt] for single hard test case:", bt_time)
    # print("Solving...")
    # print("========================")
    # print_board(board) 

# t ='..5..8..18......9.......78....4.....64....9......53..2.6.........138..5....9.714.'
# main(t)