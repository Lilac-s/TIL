import sys
sys.stdin= open('input.txt')

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    res = 1

    # 가로 찾기
    for i in range(9):
        for j in range(9):
            if sudoku[i].count(j) > 1:
                res = 0

    # 세로 찾기
    for j in range(9):
        lst = []
        for i in range(9):
            lst.append(sudoku[i][j])
        if len(lst) != len(set(lst)):
            res = 0

    # 3x3 찾기(대각선)
    for k in range(0, 9, 3):
        lst = []
        for i in range(3):
            for j in range(3):
                lst.append(sudoku[i+k][j+k])
        if len(lst) != len(set(lst)):
            res = 0

    # 3x3 찾기
    for k in range(0, 9, 3):
        lst = []
        for i in range(3):
            for j in range(3):
                lst.append(sudoku[i][j+k])
        if len(lst) != len(set(lst)):
            res = 0

        # 3x3 찾기
        for k in range(0, 9, 3):
            lst = []
            for i in range(3):
                for j in range(3):
                    lst.append(sudoku[i+k][j])
            if len(lst) != len(set(lst)):
                res = 0
    print(f'#{tc} {res}')

