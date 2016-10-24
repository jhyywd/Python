# coding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVR

def load_data():
    df = pd.read_csv("C:/Users/JYL-Family/Advertising.csv")
    x = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']

    return x, y

if __name__ == "__main__":
    x, y = load_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    ''' ʹ�����Իع�Ԥ�� '''

    lr = LinearRegression()
    lr.fit(x_train, y_train)
    lr_y_test_hat = lr.predict(x_test)
    lr_mse = np.average(((lr_y_test_hat - y_test)**2))

    ''' ʹ�ø�˹�˺���Ԥ�� '''

#    svr_rbf = SVR(kernel='rbf', gamma=0.001, C=10)
#    svr_rbf.fit(x_train, y_train)
#    svr_y_test_hat = svr_rbf.predict(x_test)
#    svr_rbf_mse = np.average(((svr_y_test_hat - y_test) ** 2))

    model = SVR(kernel='rbf')
    c_can = np.logspace(-5, 5, 5)  #
    gamma_can = np.logspace(-5, 5, 5)

    # GridSearchCV() ������֤����
    # param_grid={'C':c_can, 'gamma':gamma_can} ���� C �� c_can ��ȡ�� ���� gamma �� gamma_can ��ȡ��
    # cv = 10 ������ 10 �۽�����֤ Cross-validation
    svr_rbf = GridSearchCV(model, param_grid={'C':c_can, 'gamma':gamma_can}, cv = 10)
    svr_rbf.fit(x_train, y_train)
    print "��Ѳ�����", svr_rbf.best_params_ # ��Ѳ���Ҫѵ����֮����ܸ��� fit ֮��

    svr_y_test_hat = svr_rbf.predict(x_test)
    svr_rbf_mse = np.average(((svr_y_test_hat - y_test) ** 2))

    ''' sklearn ���Իع� ���ݿ��ӻ� '''

    x = np.arange(len(x_test))

    # ���Իع�Ԥ���������
    plt.plot(x,\
             lr_y_test_hat,\
             'r-',\
             linewidth=2,\
             label='linearregression predict')

    # svr Ԥ���������
    plt.plot(x, \
             svr_y_test_hat,\
             'b-',\
             linewidth=2,\
             label='svr predict')

    # ������ʵ����
    plt.plot(x, \
             y_test, \
             'g-', \
             linewidth=1, \
             label='predict')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()

    print lr_mse
    print svr_rbf_mse