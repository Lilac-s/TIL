# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def dec_to_bin(n):
    b = ''
    a = n % 2
    b += str(a)
    if n <= 1:
        return b
    return b, dec_to_bin(n // 2)

# ''.join(reversed(b))

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010