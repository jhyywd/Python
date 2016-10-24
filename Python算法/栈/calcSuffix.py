# coding:utf-8

def calcSuffix(str):

    # ���������
    operator = {
        '+':lambda op1, op2: op1+op2,
        '-':lambda op1, op2: op1-op2,
        '*':lambda op1, op2: op1*op2,
        '/':lambda op1, op2: op1/op2
    }

    # ջ�����洢
    stack = []

    # ��׺���ʽ�����ַ�������ʽ������ , ��������������ͨ���ո�ָ�
    # ͨ�� split() ���������֡��������ָ���һ�б��������������
    parts = str.split()

    for part in parts:
        # ��������֣��ַ���ʽ�� , ѹջ
        # int() ���� , ǿ��ת��������
        if part.isdigit():
            stack.append(int(part))
        # ����ǲ����� , ����ջ������Ԫ�� , ���ڼ���
        # ����������ѹ��ջ��
        elif part in operator:
            operation = operator[part]
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(operation(op1, op2))

    # ���ջ��ֻ��һ��Ԫ�� , ���Ǻ�׺���ʽ������
    return stack[-1]

if __name__ == '__main__':

    print calcSuffix('2 3 4 * +')