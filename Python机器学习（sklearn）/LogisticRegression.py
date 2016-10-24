# coding:utf-8

from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split

if __name__ == "__main__":
    path = "C:/Users/JYL-Family/Documents/iris.data"

    '''ͨ�� pandas ���������'''

    # ע������ header=None ��������û�б�ͷ
    data = pd.read_csv(path, header=None)

    '''ͨ�� sklearn ������Ԥ����'''

    # ȡ������� ndarray
    # ��һ�� : ����ȡ���е���
    # �ڶ��� : ����ȡ���е��� , �ӵ� 1 �п�ʼֱ����� 1 �е���������� 1 ��
    x = data.values[:, :-1]
    # ȡ������� ndarray
    y = data.values[:, -1]

    # ���������д���ʵ���˽� 'Iris-setosa' , 'Iris-versicolor' , 'Iris-virginica' ����Ϊ 0 1 2
    le = LabelEncoder()
    le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    y = le.transform(y)

    '''sklearn logistic �ع�'''

    # ����Ԥ����õ��� x , y ���ݼ�����Ϊѵ����
    x_train, x_test, y_train, y_test = train_test_split(x, y, \
                                                        test_size=0.4, random_state=1)

    logReg = LogisticRegression()
    logReg.fit(x_train, y_train.ravel())

    y_test_hat = logReg.predict(x_test)
    accuratearray = y_test_hat == y_test
    accuraterate = np.count_nonzero(accuratearray)/len(accuratearray)
    print accuraterate, '\n'

    # StandardScaler() Ӧ����ôʹ�ã����汨�˴� , ��֪����ô���
    # logReg = Pipeline([('sc', StandardScaler()), ('clf', LogisticRegression())])
    # logReg.fit(x_train, y_train.ravel())
    # y_test_hat = logReg.predict(x_test)
    # accuratearray = y_test_hat == y_test
    # accuraterate = np.count_nonzero(accuratearray)/len(accuratearray)
    # print accuraterate, '\n'


'''
    sklearn logistic �ع� ���ݿ��ӻ�
    # ���ӻ�ֻ����ǰ��������ѵ�� LR ģ��
    logReg2 = LogisticRegression()
    print logReg2.fit(x_train[:, :2], y_train)

    # Ϊ��ͼ���� , ȡ x_train ǰ���зֱ���Ϊ x ������� y �����
    x_train = x_train[:, :2]
    # x_train ��һ����Ϊ x ����� x_min, x_max �ֱ�Ϊ x ������ķ�Χ
    x_min, x_max = x_train[:, 0].min(), x_train[:, 0].max()
    # x_train ��һ����Ϊ y ����� y_min, y_max �ֱ�Ϊ y ������ķ�Χ
    y_min, y_max = x_train[:, 1].min(), x_train[:, 1].max()

    # ���� 500 ������ �� x_min ��ʼ x_max �����ĵȲ�����
    t1 = np.linspace(x_min, x_max, 2000)
    # ���� 500 ������ �� y_min ��ʼ y_max �����ĵȲ�����
    t2 = np.linspace(y_min, y_max, 2000)

    x1, x2 = np.meshgrid(t1, t2)
    print t1, '\n', t2
    print x1, '\n', x2
    x_test = np.stack((x1.flat, x2.flat), axis=1)

    y_test_hat = logReg2.predict(x_test)
    y_test_hat = y_test_hat.reshape(x1.shape)
    plt.pcolormesh(x1, x2,\
                   y_test_hat,\
                   cmap=plt.cm.Spectral,\
                   alpha=0.1)
    # c color ���� c=y_train ���� R ������ color=���Ա���
    # edgecolors='k' ԲȦ�߽��Ǻ�ɫ
    # cmap=plt.cm.prism ʹ�� plt.cm.prism ��ɫ�棿
    plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, \
                edgecolors='k', cmap=plt.cm.prism)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid()
    plt.show()
'''
