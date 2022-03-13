cnt = int(input()) # 5
bun_lst = list(map(int, input().split())) # 0 1 1 3 2
stu_lst = list(range(1, cnt+1)) # 1 2 3 4 5

for i in range(len(stu_lst)):
    a = stu_lst.pop(i) # i = 0, a = 1
    stu_lst.insert(i - bun_lst[i], a)

# 1 2 3 4 5
# 2 1 3 4 5
# 2 3 1 4 5
# 4 2 3 1 5
# 4 2 5 3 1

print(' '.join(map(str, stu_lst)))