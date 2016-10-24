# coding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# ����ʮ�ֽ�����֤
from sklearn.cross_validation import train_test_split
# �������Իع�
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    path = "C:/Users/JYL-Family/Documents/Advertising.csv"

    '''ͨ�� numpy ����� .csv ����'''
    # �ṩ·�����ļ��ö��ŷָ���������һ��
    # ���� ndarray ����
    p = np.loadtxt(path,\
                   delimiter=',',\
                   skiprows=1)
    print p

    '''ͨ�� pandas ����� .csv ����'''
    # ֻ�ṩ·������
    data = pd.read_csv(path)
    # ȡ TV��Radio��Newspaper ������
    print data[['TV', 'Radio', 'Newspaper']]

    '''���ݿ��ӻ�-1'''
    # plt.plot(x����, y����, ��״, ��ǩ)
    # ��״���ﻹ�Ǻ������ ,
    #     ro ���� red Բ��
    #     g^ ���� green ������ϵ�����
    #     bv ���� blue ������µ�����
    plt.plot(data[['TV']],\
             data[['Sales']],\
             'ro',\
             label='TV')
    plt.plot(data[['Radio']], \
             data[['Sales']], \
             'g^', \
             label='Radio')
    plt.plot(data[['Newspaper']], \
             data[['Sales']], \
             'bv', \
             label='Newspaper')
    # ͼ����ͼ�����·���ʾ
    plt.legend(loc='lower right')
    # ͼ������������
    plt.grid()
    # ͼ��ʾ
    plt.show()

    '''���ݿ��ӻ�-2������'''
    # ȷ��������С , �ⲽ����ʡ��
    plt.figure(figsize=(9 , 12))
    # 311 ����һ������ 3��1 ��ͼ , ���ڻ��Ƶ�һ��
    plt.subplot(311)
    plt.plot(data[['TV']],\
             data[['Sales']],\
             'ro')
    plt.title('TV')
    plt.grid() # ÿ��ͼ��Ҫ��
    # ͬ�� ���ڻ��Ƶڶ���
    plt.subplot(312)
    plt.plot(data[['Radio']],\
             data[['Sales']],\
             'g^')
    plt.title('Radio')
    plt.grid() # ÿ��ͼ��Ҫ��
    # ͬ�� ���ڻ��Ƶ�����
    plt.subplot(313)
    plt.plot(data[['Newspaper']],\
             data[['Sales']],\
             'bv')
    plt.title('Newspaper')
    plt.grid() # ÿ��ͼ��Ҫ��
    plt.show()

    '''sklearn ���Իع�'''

    # ���ɲ��Լ���ѵ����
    # random_state ����������������� R �����е� set.seed() �趨��ͬ���� , ��֤�´εõ���ѵ���������Լ���ͬ
    # test_size ���Լ�ռ�����ݼ��ı���
    x_train, x_test, y_train, y_test = train_test_split(data[['TV', 'Radio']],\
                                                        data[['Sales']], test_size=0.4, random_state=1)
    print len(x_train)
    print len(x_test)
    # ͨ��ѵ�������� ��0����1����2����3
    linReg = LinearRegression()
    model = linReg.fit(x_train, y_train)
    # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    # copy_X=True True ��ʾ�����ݼ� x_train��y_train �ǿ�������ʹ��
    # fit_intercept=True True ��ʾ�ṩ�����ݼ�û��ȫ 1 ��һ�� , False ��ʾ�ṩ�����ݼ��Ѿ���ȫ 1 ����һ����
    # n_jobs=1 ��һ�� cpu �ϼ���
    # normalize=False ������
    print model
    # ���� ��1����2����3
    print linReg.coef_
    # ���� ��0
    print linReg.intercept_

    # ѵ���õ�ģ�� linReg �ڲ��Լ�����Ԥ�� , �õ� x_test ��Ԥ��ֵ y_hat
    y_hat = linReg.predict(np.array(x_test))
    # ���ƽ����ƽ��ֵ �������
    mse = np.average((y_hat - np.array(y_test))** 2)
    # ���ƽ����ƽ��ֵ�ٿ����� ����������
    print mse, np.sqrt(mse)

    '''sklearn ���Իع� ���ݿ��ӻ�'''
    x = np.arange(len(x_test))
    # Ԥ���������
    plt.plot(x,\
             y_hat,\
             'r-',\
             linewidth=2,\
             label='predict')
    # ������ʵ����
    plt.plot(x, \
             y_test, \
             'g-', \
             linewidth=2, \
             label='predict')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()



