# coding:utf-8

from collections import deque

def a_to_b(a, b):
    # ��Ԫ���������ݽṹ��ʾ (������, ����)
    # ͨ��������֪ͨ�����μ����� a �õ� b
    q = deque()
    cur = (a, 0)

    # ��������������� b , �ٴμ��� ��������+1��-1��*2 ���
    while not cur[0] == b:
        # ʹ�ø��Եı����洢�������
        q.append((cur[0] + 1, cur[1] + 1))
        q.append((cur[0] - 1, cur[1] + 1))
        q.append((cur[0] * 2, cur[1] + 1))
        cur = q.popleft()
    return cur[1]

if __name__ == "__main__":
    print u'ͨ��', a_to_b(3, 11), u'�μ���ʵ�֣�'
