import sys
sys.stdin= open('sample_input(2).txt')

def binery_search(target, data):
    start = 0
    end = N-1
    direction = 0

    while start <= end:
        mid = (start+end)//2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
            if direction == 'right':
                return False
            direction = 'right'
        else:
            end = mid - 1
            if direction == 'left':
                return False
            direction = 'left'
    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # A와 B에 속한 정수의 개수
    A_lst = sorted(list(map(int, input().split())))
    B_lst = list(map(int, input().split()))
    res = 0

    for b in B_lst:
        tmp = binery_search(b, A_lst)
        if tmp:
            res += 1

    print(f'#{tc} {res}')
