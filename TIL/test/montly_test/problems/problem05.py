# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_length(password):
    # len 함수를 통해 password의 길이를 구한다.
    l = len(password)
    # 비밀번호가 8자 이상이면서 32자 이하인지 확인한다.
    if l >= 8 and l <= 32:
        # 조건에 맞다면 True를 리턴한다.
        return True
    # 그 외의 상황에서는 else를 사용한다.
    else:
        #False를 리턴한다.
        return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    password = 'q1w2e3r4'
    print(check_password_length(password)) # True
