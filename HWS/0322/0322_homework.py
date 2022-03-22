# swea_subtree
# 여러 번의 재시도가 있었어요

def subtree(x):
    global cnt
    if node[x][0] != 0:
        cnt += 1
        subtree(node[x][0])
    if node[x][1] != 0:
        cnt += 1
        subtree(node[x][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node_pairs = list(map(int, input().split()))
    node = list([0]*2 for _ in range(E+2))

    for i in range(0, len(node_pairs), 2):
        if node[node_pairs[i]][0] == 0:
            node[node_pairs[i]][0] = node_pairs[i+1]
        elif node[node_pairs[i]][0] != 0:
            node[node_pairs[i]][1] = node_pairs[i+1]

    cnt = 1
    subtree(N)
    print(f'#{tc} {cnt}')



# def res(N):
#     global cnt
#     if des1[N]:
#         cnt += 1
#         res(des1[N])
#     if des2[N]:
#         cnt += 1
#         res(des2[N])
#
# T = int(input())
# for tc in range(1, T+1):
#     E, N = map(int, input().split())
#     node_pairs = list(map(int, input().split()))
#     des1 = [0]*(E+2)
#     des2 = [0]*(E+2)
#
#     for i in range(0, len(node_pairs), 2):
#         if des1[node_pairs[i]] == 0:
#             des1[node_pairs[i]] = node_pairs[i+1]
#         else:
#             des2[node_pairs[i]] = node_pairs[i+1]
#
#     cnt = 1
#     res(N)
#     print(cnt)



#     '''node_cnt = [0]*(E*2+1)
#     for i in range(0, E*2, 2):
#         node_cnt[node_pairs[i]] += 1
#
#     for k in range(1, E*2, 2):
#         if node_cnt[node_pairs[k]] == False:
#             node_cnt[node_pairs[k]] += 1
#
#     for j in range(1, E*2, 2):
#         if node_cnt[node_pairs[j]] == True:
#             node_cnt[node_pairs[j-1]] += node_cnt[node_pairs[j]]
#
#     print(node_cnt)
#     print(node_cnt[N])'''