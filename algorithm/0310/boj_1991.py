import sys
N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right] # 주어진 input값 그대로, root에 따라서 left와 rigth를 설정해 놓는다.

def preorder(root): # 전위 순회(root > left > right)
    if root != '.': # 만일 root가 존재한다면
        print(root, end='') # root부터 출력하고
        preorder(tree[root][0]) # root의 left자식 방향으로 재귀를 먼저 돌고,
        preorder(tree[root][1]) # 그 다음으로 root의 right 자식으로 가서 재귀를 돈다.

# 아래의 중위 순회와 후위 순회도 같은 방식이다.
# 각자 순회하는 순서에 따라 재귀를 호출하고, 출력한다.

def inorder(root): # 중위 순회(left > root > right)
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root): # 후위 순회(left > right > root)
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

# 노드의 이름을 A부터 차례대로 알파벳 대문자로 매겨지고, 항상 A가 루트 노드가 된다.
preorder('A')
print()
inorder('A')
print()
postorder('A')