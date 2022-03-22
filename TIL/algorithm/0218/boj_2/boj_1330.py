A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

    # <<, >>는 비트 쉬프트 연산이야