# coding:utf-8

def initMaze():
    # ��ʼ��һ���յ� 7��7 ���
    maze = [[0] * 7 for i in range(0, 7)]
    # �Թ��ϰ���λ��
    walls = [(1, 3),(1, 5),
            (2, 1), (2, 5),
            (3, 3), (3, 4),
            (4, 2),
            (5, 4)]

    # �����һȦ���ó� 1
    for i in range(0, 7):
        maze[0][i] = 1
        maze[i][0] = 1
        maze[6][i] = 1
        maze[i][6] = 1
    # �Թ��ϰ�λ�����ó� 1
    for i, j in walls:
        maze[i][j] = 1

    return maze

def path(maze, start, end):
    # i, j ��������λ��
    i, j = start
    # ei, ej �����յ��λ��
    ei, ej = end

    # ��ջ���洢���Թ���·��
    stack = []
    # �� �� �� �����
    stack.append((i, j))
    # �� �� �� ����� , ���߹���λ����Ϊ 1
    maze[i][j] = 1

    # ѭ��һ�� , �൱�� �� �� ��  ��һ��
    # ���ջΪ�� , ������ѭ�� , ��ջ�����Թ��߲�ͨ
    while stack:
        i, j = stack[-1]
        # �� �� �� ��ʱλ���Ѿ����յ� , ����ѭ��
        if (i, j) == (ei, ej):
            break

        # ѭ���Ĵγ����ܷ����ĸ�������
        # �� di , dj ������������ʽ��ʾ �� �� �� ��һ���ľ���
        # ����������� 4 ������
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            # ������������ 0 ��������
            if maze[i+di][j+dj] == 0:
                # �� �� �� �ߵ����λ��
                stack.append((i+di, (j+dj)))
                # ���λ����Ϊ 1 , �����ߵ������λ��
                maze[i+di][j+dj] = 1
                break
        # �ĸ������� 1 ������·���ߺ���һ��
        else:
            stack.pop()

    return stack

if __name__ == '__main__':

     print path(initMaze(), (1, 1), (5, 5))