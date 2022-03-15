# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행한다.
# 주어진 수의 순서를 바꾸면 안 된다.
from itertools import permutations

N = int(input()) # 수의 개수
Ai_lst = list(map(int, input().split()))
oper_cnt = list(map(int, input().split()))
oper_lst = ['+', '-', '*', '/']
operator = []

for i in range(4):
    for j in range(oper_cnt[i]):
        operator.append(oper_lst[i])
# print(operator)
oper_npr = list(permutations(operator, len(operator)))
print(oper_npr)

res = []
for i in oper_npr:
    n = Ai_lst[0]
    for j in range(len(Ai_lst)-1):
        if i[j] =='+':
            n += Ai_lst[j+1]
        if i[j] =='-':
            n -= Ai_lst[j+1]
        if i[j] =='*':
            n *= Ai_lst[j+1]
        if i[j] =='/':
            if n//Ai_lst[j+1] <0:
                n = -(-n//Ai_lst[j+1])
            else:
                n = n//Ai_lst[j+1]
        res.append(n)
print(max(res))
print(min(res))
