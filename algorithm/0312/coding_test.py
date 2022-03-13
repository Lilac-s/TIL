def solution(money, costs):
    cost_lst = costs

    for i in range(5):
        if i % 2 == 0:
            if cost_lst[i + 1] > cost_lst[i] * 5:
                cost_lst[i + 1] = cost_lst[i] * 5
        if i % 2 == 1:
            if cost_lst[i + 1] > cost_lst[i] * 2:
                cost_lst[i + 1] = cost_lst[i] * 2

    a = money // 500
    b = (money % 500) // 100
    c = ((money % 500) % 100) // 50
    d = (((money % 500) % 100) % 50) // 10
    e = ((((money % 500) % 100) % 50) % 10) // 5
    f = (((((money % 500) % 100) % 50) % 10) % 5) // 1

    answer = a * cost_lst[5] + b * cost_lst[4] + c * cost_lst[3] + d * cost_lst[2] + e * cost_lst[1] + f * cost_lst[0]
    return answer