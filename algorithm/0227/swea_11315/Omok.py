import sys
sys.stdin= open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Pan = [list(input()) for _ in range(N)]
    omok = ['o', 'o', 'o', 'o', 'o']
    res = 'NO'

    for i in range(N):
        for j in range(N-4):
            if Pan[i][j:j+5] == omok:
                res = 'YES'

    for j in range(N):
        o_lst = []
        for i in range(N):
            o_lst.append(Pan[i][j])
        for k in range(N-4):
            if o_lst[k:k+5] == omok:
                res = 'YES'

    # 왼쪽 위에서 오른쪽 아래로 내려오는 대각선
    # 오른쪽으로 가면서 찾기
    for r in range(N-4):
        i = r
        cnt = 0
        j = 0
        while i<N and j<N:
            if Pan[i][j] == 'o':
                cnt += 1
                i += 1
                j += 1
                if cnt >= 5:
                    res = 'YES'
                    break
            elif Pan[i][j] == '.':
                cnt = 0
                i += 1
                j += 1

    # 아래로 내려가면서 찾기
    for c in range(N-4):
        i = 0
        cnt = 0
        j = c
        while i<N and j<N:
            if Pan[i][j] == 'o':
                cnt += 1
                i += 1
                j += 1
                if cnt >= 5:
                    res = 'YES'
                    break
            elif Pan[i][j] == '.':
                cnt = 0
                i += 1
                j += 1

    # 오른쪽 위에서 왼쪽 아래로 내려오는 대각선
    # 아래로 내려가며 찾기
    for r in range(N-4):
        cnt2 = 0
        ii = r
        jj = -1
        while ii<N and -jj<=N:
            if Pan[ii][jj] == 'o':
                cnt2 += 1
                ii += 1
                jj -= 1
                if cnt2 >= 5:
                    res = 'YES'
                    break
            elif Pan[ii][jj] == '.':
                cnt2 = 0
                ii += 1
                jj -= 1

    # 왼쪽으로 가며 찾기
    for c in range(1, N-3):
        cnt2 = 0
        ii = 0
        jj = -c
        while ii<N and -jj<=N:
            if Pan[ii][jj] == 'o':
                cnt2 += 1
                ii += 1
                jj -= 1
                if cnt2 >= 5:
                    res = 'YES'
                    break
            elif Pan[ii][jj] == '.':
                cnt2 = 0
                ii += 1
                jj -= 1

    print(f'#{tc} {res}')