# coding:utf-8

def match(expr):

    # ����������
    LEFT = {'{', '(', '['}
    # ����������
    RIGH = {'}', ')', ']'}

    expr = filter(lambda char: True if char in LEFT | RIGH else False, expr)

    # ���б������洢������������
    stack = []

    for char in expr:
        # ����������� , ��ջ
        if char in LEFT:
            stack.append(char)
        # �����������
        elif char in RIGH:
            # �����ʱ�Ѿ��ǿ�ջ , ˵�������Ŷ��� , ƥ�����
            if not stack:
                return u'ƥ����� �������Ŷ�'
            # �����ʱջ��Ԫ���������� , ƥ�䲻�� , ƥ�䱨��
            elif not 0 < ord(char) - ord(stack[-1]) <= 2:
                return u'ƥ����� ��ƥ�䲻��'
            # ƥ��ɹ� , ջ��Ԫ�س�ջ
            stack.pop()

    if not stack:
        return u'ƥ��ɹ�'
    # ƥ����� , �ǿ�ջ , ˵�������Ŷ��� , ƥ�����
    else:
        return u'ƥ����� �������Ŷ�'


if __name__ == '__main__':

    expr = '{{d(a[]a)}+}'

    print match(expr)




