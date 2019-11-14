f = open("easy.txt", "r")

arr = f.readlines()

sudokus = []
interSudoku = []
for line in arr:
    if("=" in line):
        sudokus.append(interSudoku)
        interSudoku = []
    else:
        interSudoku.append(line)
print(sudokus)
for sudoku in sudokus:
    for line in sudoku:
        for c in line[:-1]:
            # if(c=="0"):
            #     print(".", end="", sep="")
            # if(c=="\n"):
            #     print("", end="", sep="")
            # else:
            #     print(c, end="", sep="")
            if(c=="0"):
                print(".", end="", sep="")
            # if(c=="\n"):
            #     print("", end="", sep="")
            else:
                print(c, end="", sep="")
    print("")
