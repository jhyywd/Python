# coding:utf-8

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

def show_accuracy(y_test, y_test_hat):
    acc_number = sum(y_test == y_test_hat)
    acc_rate = float(acc_number)/len(y_test)
    return np.round(acc_rate, 2)

def load_data():
    # ������
    df = pd.read_csv("C:/Users/JYL-Family/Titanic_train.csv")


    # Sex �Ա��������� , �� female��male ��Ϊ 0��1 sklearn ���ܹ�����
    df.Sex = df.Sex.map({'female': 0, 'male': 1}).astype(int)


    # Fare ��Ʊ�۸��������� , ����ͬ��λ��Ʊ�۸����λ������
    if sum(df.Fare.isnull()) > 0: # �����Ʊ�۸���ȱʧֵ
        fare = np.zeros(3)
        # ����������λ��Ʊ�۸����λ�� , �洢�� fare �б���
        for f in range(0, 3):
            fare[f] = df.loc[df.Pclass == f + 1, 'Fare'].dropna().median()
        # ѭ���� fare �б��еĴ�Ʊ�۸���ӵ���Ӧ��λ�ġ� ��Ʊ�۸�ȱʧ��
        for f in range(0, 3):
            df.loc[(df.Fare.isnull()) & (df.Pclass == f + 1), 'Fare'] = fare[f]


    # Age ������������ , ʹ�����ɭ�ֲ���Ԥ������
    df_for_age = df[['Age', 'Survived', 'Fare', 'Parch', 'SibSp', 'Pclass']]
    age_exist = df_for_age.loc[(df.Age.notnull())]   # ���䲻ȱʧ������ , ��Ϊѵ����
    age_null = df_for_age.loc[(df.Age.isnull())]     # ����ȱʧ������ , ��Ϊ��ʵ����������
    
    x = age_exist.values[:, 1:] # ѵ�����������
    y = age_exist.values[:, 0]  # ѵ�����������
    
    rfr = RandomForestRegressor(n_estimators=1000) # ���� 1000 ���������ɭ�ֶ��������Ԥ��
    rfr.fit(x, y) 
    age_hat = rfr.predict(age_null.values[:, 1:])

    df.loc[(df.Age.isnull()), 'Age'] = age_hat


    # Embarked ���������������� , ʹ����������������ȱʧֵ��
    df.loc[(df.Embarked.isnull()), 'Embarked'] = \
        df.loc[df.Embarked.notnull(), 'Embarked'].mode().get_values() # ����.mode() ���ص��� Series ����,Ҫʹ�� get_values()
    
    embarked_df = pd.get_dummies(df.Embarked) 
    embarked_df = embarked_df.rename(columns=lambda x: 'Embarked_' + str(x))
    df = pd.concat([df, embarked_df], axis=1)

    x = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_C', 'Embarked_Q', 'Embarked_S']]
    y = df['Survived']


    # �������ݼ�����������������ѵ������Ŀ�� , x ���ݼ����� 3 �� , y ���ݼ����� 3 ��
    x = np.array(x)
    y = np.array(y)
    x = np.tile(x, (3, 1)) # �в����� , ÿ�и��� 3 ��
    y = np.tile(y, (3, ))  # �в����� , ÿ�и��� 3 ��


    return x, y


if __name__ == "__main__":
    
    # ����¼��
    x, y = load_data()

    # ����ѵ���� �����Լ�
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=1)
    
    # ʹ�� LR Ԥ�� Survived
    lr = LogisticRegression(penalty='l2')
    lr.fit(x_train, y_train)
    y_test_hat = lr.predict(x_test)
    lr_rate = show_accuracy(y_test, y_test_hat)
    
    
    # ʹ�� RF Ԥ�� Survived
    rfc = RandomForestClassifier(n_estimators=1000)
    rfc.fit(x_train, y_train)
    y_test_hat = rfc.predict(x_test)
    rfc_rate = show_accuracy(y_test, y_test_hat)
    
    # ʹ�� GBDT Ԥ�� Survived
    gbc = GradientBoostingClassifier()
    gbc.fit(x_train, y_train)
    y_test_hat = gbc.predict(x_test)
    gbc_rate = show_accuracy(y_test, y_test_hat)

    print 'Logistic�ع飺%f' % lr_rate
    print '���ɭ�֣�%f' % rfc_rate
    print 'GBDT��%f' % gbc_rate