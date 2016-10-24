# coding:utf-8

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import  train_test_split
from sklearn.preprocessing import LabelEncoder

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

    # ����ѵ���� ���Լ���ʱ�� ����д��������ʽ
    # train_test_split(x) train_test_split(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    '''sklearn  ���ɭ�� ������'''

    # n_estimators=10 ���� 10 �þ�����
    rf_clf = RandomForestClassifier(criterion="entropy", n_estimators=10)
    rf_clf.fit(x_train, y_train)
    y_test_hat = rf_clf.predict(x_test)

    print float(np.count_nonzero(y_test_hat==y_test))/len(y_test)
    print np.round(float(np.count_nonzero(y_test_hat==y_test))/len(y_test), 4) * 100
