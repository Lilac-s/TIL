# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def caesar(word, n):
    # 빈 문자열 b를 만든다.
    b = ''
    # word 의 길이만큼 반복하는 반복문을 만든다.
    for i in range(len(word)):
        # a를 10진수 값으로 바꾸고 정수 n만큼 민다.
        a = ord(word[i]) + n
        # n 만큼 밀린 정수인 a를 다시 아스키 코드를 통한 문자로 바꾼다.
        b += chr(a)
    # 바꾼 값인 b를 리턴한다.
    return b




# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx