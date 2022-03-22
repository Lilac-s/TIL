import sys
sys.stdin= open('input.txt')

for _ in range(10):
    tc = int(input())
    char_lst = [list(input()) for a in range(100)]
    pal_lst = []
    # print(tc)
    # print(char_lst)

    # 행 회문 찾기
    for i in range(100):
        row_lst = []
        for j in range(100):
            row_lst.append(char_lst[i][j])
        row_lst.reverse()


    # 열 회문 찾기
    col_lst = []
    col_lst_pal = []
    for i in range(100):
        for j in range(100):
            col_lst.append(char_lst[j][i])
            col_lst_pal.append(char_lst[j][i])
        if col_lst == col_lst_pal[::-1]:
            pal_lst.append(col_lst)
        col_lst = []
        col_lst_pal = []

    print(pal_lst)
