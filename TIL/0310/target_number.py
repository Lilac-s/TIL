def solution(numbers, target):
    answer = 0
    cal_lst = [0] # 모든 계산 결과를 받을 리스트
    for num in numbers:
        tmp = []
        for i in cal_lst:
        # cal_lst에는 이전의 계산 결과가 담겨 있다. 첫 번째 포문에서, cla_lst에는 0만 들어가 있을 것이다.
        # 그 때 num을 한번씩 더하고 뺀 값을 tmp list에 넣고 tmp를 cal_lst에 대입해 준다.
            tmp.append(i + num)
            tmp.append(i - num)
        cal_lst = tmp
        # print(cal_lst)
        # 여기서 바로 cal_lst에 append 하지 않고 tmp를 사용하는 이유는,
        # for문이 순회할수록 cal_lst는 2개씩 더 늘어나고, i는 1씩 증가하므로 cal_lst는 끝없이 증식하는 것을 막기 위함이다.
    for cal in cal_lst:
        if cal == target:
            answer += 1
    return answer

# numbers = [1, 1, 1, 1, 1]
# target = 3
# res = solution(numbers, target)
# print(res)