import sys
sys.stdin= open('input (1).txt')
for _ in range(10): # 테스트케이스 10번

    n = int(input()) # 덤프 횟수 n
    box_lst = list(map(int, input().split())) # box 리스트

    mn = 0 # box 중 최솟값을 받을 변수 mn
    mx = 0 # box 중 최댓값을 받을 변수 mx
    for k in range(n): # n 만큼 dump 실행

        for i in range(100): # 가로 길이가 100 이므로 100번 반복
            for j in range(len(box_lst)-1): # 버블 정렬
                if box_lst[j] > box_lst[j+1]:
                    box_lst[j], box_lst[j+1] = box_lst[j+1], box_lst[j]

        box_lst[0] = box_lst[0] + 1
        box_lst[-1] = box_lst[-1] - 1  # dump 실행

    # 마지막 dump를 실행하고 나서 한번 더 정렬
    # 실행하지 않은 상태로 출력하면 6번 케이스에서 15가 나온다.
    # 같은 숫자가 연속된 경우(3 3 4 5), 마지막 dump에서 반례(4 3 4 5)가 발생하기 때문인 것으로 보인다.
    for i in range(100): # 가로 길이가 100 이므로 100번 반복
        for j in range(len(box_lst)-1): # 버블 정렬
            if box_lst[j] > box_lst[j+1]:
                box_lst[j], box_lst[j+1] = box_lst[j+1], box_lst[j]

    mn = box_lst[0] # 가장 적은 box 수를 mn에 할당
    mx = box_lst[-1] # 가장 많은 box 수를 mx에 할당

    if mn + 1 < mx:
        print(f'#{_+1} {mx - mn}')
    elif mn == mx:
        print(f'#{_+1} 0')
    elif mn + 1 == mx:
        print(f'#{_+1} 1') # case를 나눠서 출력

