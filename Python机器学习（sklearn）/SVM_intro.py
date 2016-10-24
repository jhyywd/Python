# coding:utf-8

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn import svm


def show_accuracy(y_test, y_test_hat):
    # ͨ�������б�֤ y_test �� y_test_hat ���������� , �����п��� y_test ����������
    # y_test_hat ���������޷��Ƚ�
    y_test = y_test.ravel()
    y_test_hat = y_test_hat.ravel()

    acc_number = sum(y_test == y_test_hat)
    acc_rate = float(acc_number)/len(y_test)

    return acc_rate

def load_data():
    df = pd.read_csv("C:/Users/JYL-Family/Iris.csv")
    df.columns = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species'] # ���ݲ������� , �����

    x = df[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']] # �������
    y = df[['Species']] # �������

    # ���������д���ʵ���˽� 'Iris-setosa' , 'Iris-versicolor' , 'Iris-virginica' ����Ϊ 0 1 2
    le = LabelEncoder()
    le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    y = le.transform(y)

    return x, y

if __name__ == "__main__":
    x, y =  load_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # SVC �� svm ��������ķ��� , һ�����������˵�� svm ���� SVC
    # ���� SVR svm �����ع�


    clf_l = svm.SVC(C=0.8, kernel='linear', decision_function_shape='ovr')           # ʹ�����Ժ˺���
    clf_r = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')    # ʹ�ø�˹�˺���

    clf_l.fit(x_train, y_train.ravel())
    clf_r.fit(x_train, y_train.ravel())

    # clf.score() SVC �����Դ��ļ�����ȷ�ʵķ��� , ���� ( ���Լ�������� , ���Լ��������)
    print clf_l.score(x_test, y_test) # �������Ժ˺���Ч��ԶԶ���ڸ�˹�˺���
    print clf_r.score(x_test, y_test)