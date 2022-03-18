import sys
sys.stdin= open('input.txt')

cals = ['+', '-', '*', '/']

def inorder(T):
    if T >= N:
        return node[0]
    if 2*T < N and 2*T+1 < N:
        if node[T] in cals and node[2*T] in cals:
            inorder(2*T)
        if node[T] in cals and not node[2*T] in cals and node[2*T+1] in cals:
            inorder(2*T+1)
        if node[2*T] not in cals and node[2*T+1] not in cals:
            if node[T] == '+':
                node[T] = int(node[2*T]) + int(node[2*T+1])
            if node[T] == '-':
                node[T] = int(node[2*T]) - int(node[2*T+1])
            if node[T] == '*':
                node[T] = int(node[2*T]) * int(node[2*T+1])
            if node[T] == '/':
                if int(node[2*T+1]) == 0:
                    node[2*T+1] = 1
                node[T] = int(node[2*T]) / int(node[2*T+1])

for tc in range(1, 11):
    N = int(input())
    node = [0]*(N+1)
    leaf_lst = []
    for _ in range(N):
        leaf = list(input().split())
        leaf_lst.append(leaf)

    for i in range(N):
        if len(leaf_lst[i]) == 4:
            node[int(leaf_lst[i][0])] = leaf_lst[i][1]
            for j in range(N):
                if leaf_lst[i][2] == leaf_lst[j][0]:
                    node[int(leaf_lst[j][0])] = leaf_lst[j][1]
                if leaf_lst[i][3] == leaf_lst[j][0]:
                    node[int(leaf_lst[j][0])] = leaf_lst[j][1]

    print(node)
    a = inorder(1)
    print(a)