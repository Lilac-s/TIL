# 0224_homework



## boj_2628

```python
R, C = map(int, input().split())
line = int(input())
col_cut = []
row_cut = []

for i in range(line):
    A, B = map(int, input().split())
    if A == 0:
        col_cut.append(B)
    elif A == 1:
        row_cut.append(B)

col_cut.append(C)
row_cut.append(R)

col_cut.sort()
row_cut.sort()
# print(col_cut)
# print(row_cut)

mx_col = 0
mx_row = 0

for c in range(1, len(col_cut)):
    col = col_cut[c] - col_cut[c-1]
    if mx_col <= col:
        mx_col = col

for r in range(1, len(row_cut)):
    row = row_cut[r] - row_cut[r-1]
    if mx_row <= row:
        mx_row = row

print(mx_row*mx_col)
```



## boj_2635

```python
A = int(input())

if A == 1:
    print(4)
    print('1 1 0 1')

else:
    mx_lst = []
    for B in range(1, A):
        C = A - B
        Ai_lst = [A, B, C]
        D = B - C

        while D>=0:
            D = Ai_lst[-2]-Ai_lst[-1]
            if D>=0:
                Ai_lst.append(D)
            else:
                break

        if len(Ai_lst) > len(mx_lst):
            mx_lst = Ai_lst

    print(len(mx_lst))
    print(*mx_lst)
```



## boj_2669

```python
grid = [[0]*100 for g in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

    cnt = 0
    for a in grid:
       cnt += sum(a)

print(cnt)
```

