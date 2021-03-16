from pprint import pprint

def nextrc(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i,j
    return None,None

def isvalid(puzzle,r,c,temp):

    for i in range(9):
        if puzzle[r][i] == temp:
            return False
    for i in range(9):
        if puzzle[i][c] == temp:
            return False
    row = (r//3)*3
    col = (c//3)*3
    for i in range(row,row+3):
        for j in range(col,col+3):
            if puzzle[i][j] == temp:
                return False
    return True


def solve(puzzle):
    r , c = nextrc(puzzle)
    if r is None:
        return True
    for i in range(1,10):
        if isvalid(puzzle,r,c,i):
            puzzle[r][c]=i
            if solve(puzzle):
                return True
        puzzle[r][c]=-1
    return False


if __name__ == '__main__':
    li = []
    print("enter")
    for i in range(9):
        li.append(list(map(int,input().split())))
    solve(li)
    pprint(li)
