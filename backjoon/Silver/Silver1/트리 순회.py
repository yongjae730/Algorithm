def preorder(node):

    if node == 0:
        return

    print(node, end='')
    preorder(left[arr.index(node)])
    preorder(right[arr.index(node)])
def inorder(node):

    if node == 0:
        return

    inorder(left[arr.index(node)])
    print(node, end='')
    inorder(right[arr.index(node)])
def postorder(node):

    if node == 0:
        return

    postorder(left[arr.index(node)])
    postorder(right[arr.index(node)])
    print(node, end='')



arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']

N = int(input())

left = [0] * (N + 1)
right = [0] * (N + 1)

for _ in range(N):
    node, l_child, r_child = map(str, input().split())
    for i in range(len(arr)):
        if l_child != '.' and arr[i] == node:
            left[i]= l_child
        if r_child != '.' and arr[i] == node:
            right[i]= r_child

preorder('A')
print()
inorder('A')
print()
postorder('A')