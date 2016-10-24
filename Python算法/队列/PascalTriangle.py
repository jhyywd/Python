# coding:utf-8

from collections import deque

# k ����õ��� k ����������ͼ�ε����� ,
# Ҳ�� (a + b)^k  չ��ʽ��Ԫ�ص�ϵ��
def PascalTriangle(k):

    # ��ʼ������ , �õ�������ǵ�һ������
    q = deque([1])

    # 0       1
    # 1     1   1     �õ����Ԫ����Ҫ���� 1 ��ѭ��
    # 2    1  2  1    �õ����Ԫ����Ҫ���� 2 ��ѭ��
    # �õ��� k ��Ԫ�� , ��Ҫ k ��ѭ���������� 0 ��ʼ������
    # i ����ǰѭ�������ɵ� i ��
    for i in range(k):

        # 0       1
        # 1     1   1     ��һ����Ҫ����һ��Ԫ��
        # 2    1  2  1    �ڶ�����Ҫ���Ӷ���Ԫ��
        # �� i ����Ҫ���� i ��Ԫ�� , �������ɵ� i + 1 ��
        for _ in range(i):
            # q[0] �����ͷԪ��
            q.append(q.popleft() + q[0])

        # ��β׷��һ�� 1
        q.append(1)

    # ������ת��Ϊ�б�
    return list(q)

if __name__ == '__main__':
    print PascalTriangle(0)



