# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_duplicate_id(target_username, username_list):
    # username_list 안에 target_username이 있는지 확인한다.
    if target_username in username_list:
        # 있다면 True를 리턴한다.
        return True
    # 그렇지 않다면,
    else:
        # False를 리턴한다.
        return False
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    target_username = 'jungssafy'
    username_list = ['kimssafy', 'jungssafy']
    print(check_duplicate_id(target_username, username_list)) # True
