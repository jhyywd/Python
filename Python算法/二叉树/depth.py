# coding:utf-8

from collections import deque

class TreeNode(object):

    # data �ڵ������
    # left ��ڵ� right �ҽڵ�
    # left = None right = None Ĭ�����ɵ���Ҷ�ڵ�
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # ��д str ����
    # print TreeNode �����ʱ�� , ��ӡ����Ӧ�� data
    def __str__(self):
        return str(self.data)

def createTree():
    # ͨ���б�������ʽ��������ڵ㣨��ʱ�ڵ㶼û����ڵ����ҽڵ� , ���ǹ����ģ�
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']

    A.left = B
    A.right = C
    B.right = D
    C.left = E
    C.right = F
    E.left = G
    F.left = H
    F.right = I

    return A

def depth(node):

    if node is None:
        return 0

    dl = depth(node.left)
    dr = depth(node.right)

    return max(dl, dr) + 1

def depth2(root):
    q = deque([(root, 1)])

    while True:
        node, d = q.popleft()

        if node.left:
            q.append((node.left, d+1))
        if node.right:
            q.append((node.right, d+1))

        if not q:
            break

    return d

if __name__ == '__main__':
    print depth2(createTree())