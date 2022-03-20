# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def total(scores):
    # sum을 이용하여 scores의 모든 값을 더하고 sum_all에 할당한다.
    sum_all = sum(scores)
    # 모든 값을 더한 sum_all을 리턴한다.
    return sum_all


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(total(scores)) # 330
