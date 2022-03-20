# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_user_id(data):
    # dictionary data 의 key값인 id를 사용하여 id의 value를 가져와서 user_id 변수에 할당한다.
    user_id = data['id']
    # id 값을 가진 user_id를 리턴한다.
    return user_id


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = {
        "id": "jungssafy",
        "password": "q1w2e3r4",
        "password_confirm": "q1w2e3r4"
    }
    print(get_user_id(user_data)) # 'jungssafy'
