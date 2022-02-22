import sys
sys.stdin= open('sample_input(3).txt')

T = int(input())
for tc in range(1, T+1):
    chars = input() # input 받기

    stack = [] # append, pop 할 stack list 만들기

    for char in chars: # input 받은 chars를 순회하는 char
        if len(stack) == 0: # stack이 비어 있다면 무조건 append
            stack.append(char)
        elif char == stack[-1]: # stack의 맨 위가 새로 넣을 char과 같다면 pop 해서 없애주기
            stack.pop()
        elif char != stack[-1]: # stack의 맨 위가 새로 넣을 char과 다르다면 append 해주기
            stack.append(char)

    print(f'#{tc} {len(stack)}') # 만들어진 stack list의 len으로 출력