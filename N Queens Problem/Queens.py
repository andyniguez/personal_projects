#------------------------------------------------------------------------------ 
#  Andrew Yniguez
#  2021
#
#  Queens.py
#  This program solves the N queens problem.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------

import sys

#------------------------------------------------------------------------------
# definitions of required functions, classes etc..
#------------------------------------------------------------------------------

def placeQueen(B, i, j):
    B[i][j] = 1
    B[i][0] = j
    for y in range(i + 1, len(B) + 1): # marks all squares below queen
        if y >= len(B):
            break
        B[y][j] -= 1
    x = j
    for y in range(i + 1, len(B) + 1): # marks all squares diagonal right queen
        x += 1
        if y >= len(B) or x >= len(B):
            break
        B[y][x] -= 1
    x = j
    for y in range(i + 1, len(B) + 1): # marks all squares diagonal left queen
        x -= 1
        if y >= len(B) or x < 1:
            break
        B[y][x] -= 1
    
def removeQueen(B, i, j):
    B[i][j] = 0
    B[i][0] = 0
    for y in range(i + 1, len(B) + 1): # unmarks all squares below queen
        if y >= len(B):
            break
        B[y][j] += 1
    x = j
    for y in range(i + 1, len(B) + 1): # marks all squares diagonal right queen
        x += 1
        if y >= len(B) or x >= len(B):
            break
        B[y][x] += 1
    x = j
    for y in range(i + 1, len(B) + 1): # marks all squares diagonal left queen
        x -= 1
        if y >= len(B) or x < 1:
            break
        B[y][x] += 1
def printBoard(B):
    solution = "("
    for i in range(1, len(B)):
        if i == len(B) - 1:
            solution = solution + str(B[i][0]) + ")"
        else:
            solution = solution + str(B[i][0]) + ", "
    print(solution)

def findSolutions(B, i, mode):
    defba = 0
    if i >= len(B):
        if mode == "verbose":
            printBoard(B)
        return 1
    else:
        for x in range(1, len(B)):
            if B[i][x] == 0:
                placeQueen(B, i, x)
                defba = defba + findSolutions(B, i + 1, mode)
                removeQueen(B, i, x)
    return defba
                
    
#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("Usage: python3 Queens.py [-v] number",file=sys.stderr)
        print("Option: -v verbose output, print all solutions",file=sys.stderr)
        exit()
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            vornot = "0"
        except ValueError:
            print("Usage: python3 Queens.py [-v] number",file=sys.stderr)
            print("Option: -v verbose output, print all solutions",file=sys.stderr)
            exit()
        if n < 1 or n > 13:
            print("Usage: python3 Queens.py [-v] number",file=sys.stderr)
            print("Option: -v verbose output, print all solutions",file=sys.stderr)
            exit()
    if len(sys.argv) == 3:
        if sys.argv[1] == "-v":
            vornot = "verbose"
        else:
            print("Usage: python3 Queens.py [-v] number",file=sys.stderr)
            print("Option: -v verbose output, print all solutions",file=sys.stderr)
            exit()
        try:
            n = int(sys.argv[2]) 
        except ValueError:
            print("Usage: python3 Queens.py [-v] number",file=sys.stderr)
            print("Option: -v verbose output, print all solutions",file=sys.stderr)
            exit()
        if n < 1 or n > 13:
            print("Usage: python3 Queens.py [-v] number",file=sys.stderr)
            print("Option: -v verbose output, print all solutions",file=sys.stderr)
            exit()
    board = [[0 for i in range(n + 1)] for j in range(n + 1)]
    numsol = findSolutions(board, 1, vornot)
    print(f"{n}-Queens has {numsol} solutions")
# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end
