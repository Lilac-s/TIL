import sys
sys.stdin= open('input.txt')
for j in range(1, 11):

    n = int(input()) # 가로 길이 입력받기
    num_lst = list(map(int, input().split())) # list로 건물 높이 입력받기

    result = [] # 조망권이 확보된 칸 수를 받을 list 만들기

    for i in range(2, n-1): # 앞 뒤 00을 제외한 건물 수만큼 순환
            # 조망권이 확보된 칸의 유무를 확인하기 위한 if문 작성
            if num_lst[i] > num_lst[i-1] and num_lst[i] > num_lst[i-2] and num_lst[i] > num_lst[i+1] and num_lst[i] > num_lst[i+2]:
                # max 함수를 사용하여 칸 주변 건물 중 가장 높은 건물 추출
                high = max(num_lst[i+1], num_lst[i+2], num_lst[i-1], num_lst[i-2])
                # 조망권이 확보된 칸 = 건물 높이 - 가리는 건물 높이
                result.append(num_lst[i] - high)

    # 각각의 칸 수를 더한 값 추출
    print(f'#{j} {sum(result)}')