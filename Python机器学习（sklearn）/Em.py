# coding:utf-8

from __future__ import division
import numpy as np
from scipy.stats import norm

if __name__ == "__main__":
    # ��һ����˹�ֲ���ֵΪ 0 ����Ϊ 1
    mu1 = (1.72)
    cov1 = (0.3)
    data1 = np.random.normal(mu1, cov1, 300)
    # �ڶ�����˹�ֲ���ֵΪ 5 ����Ϊ 1
    mu2 = (1.65)
    cov2 = (0.5)
    data2 = np.random.normal(mu2, cov2, 200).T

    # ��������˹�ֲ�����ƴ�ӵ�һ��
    data = np.hstack((data1, data2))

    '''���²������ EM �㷨��'''

    # ָ����ʼ����
    pai = 0.5

    mu1hat = np.random.random(size=1) + 1 # ��ֵ , random() ��������һ�� [0, 1) �������
    cov1hat = np.random.random(size=1)    # ��׼��
    mu2hat = np.random.random(size=1) + 1
    cov2hat = np.random.random(size=1)

    for i in range(100):

        # E ����
        norm1 = norm(mu1hat, cov1hat) # �ṩ��ֵ , ��׼��
        norm2 = norm(mu2hat, cov2hat) # ���ص� norm �������ܹ����� PDF ����

        tau1 = pai * norm1.pdf(data)
        tau2 = (1-pai) * norm2.pdf(data)

        gamma1 = tau1/(tau1 + tau2)   # ������� "/" Ҫʹ�� from __future__ import division
        gamma2 = tau2/(tau1 + tau2)   # �����ʡ��С������

        # M ����
        N1 = sum(gamma1)
        N2 = sum(gamma2)

        mu1hat = np.dot(gamma1, data.T)/N1
        mu2hat = np.dot(gamma2, data.T)/N2

        cov1hat = np.sqrt(np.dot(gamma1 * (data - mu1hat).T, data - mu1hat)/N1) # ���ﷵ�ص��Ƿ��� , ������Ҫ
        cov2hat = np.sqrt(np.dot(gamma2 * (data - mu2hat).T, data - mu2hat)/N2) # np.sqrt() �õ���׼��

        pai = N1/len(data)


    print pai
    print mu1hat, mu2hat   # �������ܹ���������˹�ֲ��ֿ�
    print cov1hat, cov2hat








