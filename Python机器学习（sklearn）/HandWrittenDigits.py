#coding:utf-8

import pandas as pd
from sklearn import svm

def load_train_data():
    df = pd.read_csv("C:/Users/JYL-Family/optdigits.tra", header=None)
    x = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]

    return x, y

def load_test_data():
    df = pd.read_csv("C:/Users/JYL-Family/optdigits.tes", header=None)
    x = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]

    return x, y

def get_wrong_test_input(x_test, y_test, y_test_hat):
    df = x_test.loc[y_test != y_test_hat]
    return df

def get_wrong_test_output(x_test, y_test, y_test_hat):
    y_test = y_test.ravel()
    y_test_hat = y_test_hat.ravel()
    df_1 = y_test[y_test != y_test_hat]
    df_2 = y_test_hat[y_test != y_test_hat]
    return df_1, df_2


if __name__ == "__main__":
    x_train, y_train = load_train_data()
    x_test, y_test = load_test_data()

    clf_l = svm.SVC(C=0.8, kernel='linear', decision_function_shape='ovr')            # ʹ�����Ժ˺���
    clf_r = svm.SVC(C=0.8, kernel='rbf', gamma=0.001, decision_function_shape='ovr')  # ʹ�ø�˹�˺���

    # ����ע��һ��
    clf_l.fit(x_train, y_train.ravel())
    clf_r.fit(x_train, y_train.ravel())

    print clf_l.score(x_test, y_test)
    print clf_r.score(x_test, y_test)

    print get_wrong_test_input(x_test, y_test, clf_l.predict(x_test)) # ���� clf_l ������Ԥ���������������64 ���Ҷ�ֵ��
    true_output, wrong_output = get_wrong_test_output(x_test, y_test, clf_l.predict(x_test))
    print "----Ԥ�����----"
    print "��ʵֵ", true_output
    print "Ԥ��ֵ", wrong_output