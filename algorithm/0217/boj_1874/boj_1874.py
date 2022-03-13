n = int(input()) # 1 <= n <= 100000
count = 0
stack_lst = [] # push와 pop을 하는 스택 리스트
result = [] # 출력을 위한 + - 를 받는 result
msj = True # NO 를 출력하기 msj

for i in range(n): # n번 만큼 반복하는 for문
    # 둘쨰 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로(무작위)주어진다.
    num = int(input())

    while count < num: # 입력받은 수가 나올 때까지
      count += 1 # 카운트를 하나씩 더하면서
      stack_lst.append(count) # stack_lst에 append(push) 해준다.
      result.append("+") # stack lst에 push 되므로 result에는 +를 append 해준다.

# 위의 while문을 지나면 stack_lst에 count가 1, 2, 3, 4... 차곡차곡 쌓이게 된다.
# 다음에 들어온 num이 마지막 count와 같다면 pop을 해야 한다.
    if stack_lst[-1] == num: # 스택 리스트의 마지막 숫자가 방금 입력받은 숫자와 같으면
        stack_lst.pop() # pop을 실행해서 stack_lst에서 pop해 준다.
        result.append("-") # pop을 실행했으므로 result에 - 을 append 해준다.
    else:
        msj = False # 불가능하다면 msj에 False를 할당하여 NO를 출력한다.

if msj == False:
    print("NO")
else:
    print("\n".join(result))