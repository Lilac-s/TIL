import sys
sys.stdin= open('sample_input(4).txt')

def triplet(lst):
    new_lst = []
    for chr in lst:
        if chr not in new_lst:
            new_lst.append(chr)
    for i in range(len(new_lst)-2):
        if new_lst[i]+2 == new_lst[i+1]+1 == new_lst[i+2]:
            return 1

T = int(input())
for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    card.reverse()
    player1 = []
    player2 = []
    res = 0

    while card:
        one = card.pop()
        two = card.pop()
        player1.append(one)
        player2.append(two)
        player1.sort()
        player2.sort()
        for i in range(len(player1)):
            if player1.count(player1[i]) == 3:
                res = 1
        if triplet(player1):
            res = 1
        if res != 0:
            break

        for i in range(len(player2)):
            if player2.count(player2[i]) == 3:
                res = 2
        if triplet(player2):
            res = 2
        if res != 0:
            break

    print(f'#{tc} {res}')