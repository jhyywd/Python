# coding:utf-8

from collections import deque

# �ڵ�ͨ���ඨ�壨��������ʽ�ࣩ
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


# �������
def levelOrder(root):
    node = root
    q = deque([node])

    while True:
        node = q.popleft()
        print node

        if not node.left == None:
            q.append(node.left)

        if not node.right == None:
            q.append(node.right)

        if not q:
            break

if __name__ == "__main__":
    cengIter(createTree())