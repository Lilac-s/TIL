import sys
sys.stdin= open('sample_input(2).txt')

'''
교수님의 딕셔너리 관련 collection defaultdict, counter 설명
a = int(input())

for _ in range(a):
    tc, l = input.split()
    l = int(l)

    lst = []
    dic = {}
    # for key in lst:
    #     dic[key] = 0
    from collections import defaultdict, Counter

    #input_list=list(input().split())
    dic = Counter(list(input().split()))
    # for i in input_lst:
    #     dic[i] +=1

    print(dic)
    '''

tc = int(input())
for _ in range(tc):
    str1 = list(input())
    str2 = list(input())
    # print(str2)

    s1 = set(str1)
    # print(str1)
    cnt_dic = {}

    for s in s1:
        cnt = 0
        if s in str2:
            cnt = str2.count(s)
            cnt_dic[s] = cnt
    # print(cnt_dic)

    cnt_max = max(cnt_dic.values())
    print(f'#{_+1} {cnt_max}')

