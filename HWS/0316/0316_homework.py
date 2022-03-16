import sys
sys.stdin= open('input.txt')

def inorder(T):
    if T > N:
        return
    if (T*2) <= N:
        inorder(T*2)
    res.append(node[T])
    if (T*2+1) <= N:
        inorder(T*2+1)

for tc in range(1, 11):
    N = int(input())
    node = [0]*(N+1)
    for _ in range(N):
        lst = input().split()
        node[int(lst[0])] = lst[1]

    res = []
    inorder(1)
    print(f'#{tc} {"".join(res)}')
