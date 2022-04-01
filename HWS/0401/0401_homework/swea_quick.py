import sys
sys.stdin= open('sample_input(1).txt')

# 병합 정렬은 그냥 두 부분으로 나누는 반면에,
# 퀵 정렬을 분할할 때 pivot을 중심으로 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

def quick_sort(lst, l, r): # 퀵 정렬
    if l < r: # 만나기 전까지
        pivot = lomuto_partition(lst, l, r) # lomuto_partition을 통해 pivot을 찾는다.
        quick_sort(lst, l, pivot-1)
        quick_sort(lst, pivot+1, r) # 좁혀가면서 재귀

def lomuto_partition(lst,l,r):
    pivot = lst[r]
    i = l-1
    for j in range(l, r):
        if lst[j] <= pivot:
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[r], lst[i+1] = lst[i+1], lst[r]
    return i+1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    quick_sort(ai, 0, N-1)

    print(f'#{tc} {ai[N//2]}')