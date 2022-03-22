# boj_2578_bingo



```python
import sys
# sys.stdin= open('bingo.txt')

# 빙고판 딕셔너리
bingo_dict = dict()
for i in range(5):
    bingo_list = list(map(int, input().split()))
    for j in range(5):
        bingo_dict[bingo_list[j]] = (i, j)

# 사회자가 부를 빙고판
call = [list(map(int, input().split())) for _ in range(5)]

# 빙고 개수 확인할 배열
bingo_checker = [[0]*5 for _ in range(5)]



check_count = 0
for i in range(5):
    for j in range(5):
        bingo_checker[bingo_dict[call[i][j]][0]][bingo_dict[call[i][j]][1]] = 1
        check_count += 1
        bingo_count = 0

        dia_lst_1 = []
        dia_lst_2 = []
        dia_1 = 0
        dia_2 = 0
        # 행, 열, 대각선 빙고
        for a in range(5):
            col_lst = []
            dia_lst_1.append(bingo_checker[a][a])
            dia_lst_2.append(bingo_checker[a][-a])
            for b in range(5):
                col_lst.append(bingo_checker[a][b])
                dia_1 = sum(dia_lst_1)
                dia_2 = sum(dia_lst_2)
                col_sum = sum(col_lst)
                if sum(bingo_checker[a]) == 5:
                    bingo_count += 1
                if dia_1 == 5:
                    bingo_count += 1
                if dia_2 == 5:
                    bingo_count += 1
                if col_sum == 5:
                    bingo_count += 1

        # 빙고 체크
        if bingo_count >= 3:
            print(check_count)
            sys.exit()

```

