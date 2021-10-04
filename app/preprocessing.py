import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

from .defs import *


def application_preprocessing(input_data, train_data):

    input_data['建ぺい率（％）'] = input_data['建ぺい率（％）'].astype(float)
    input_data['容積率（％）'] = input_data['容積率（％）'].astype(float)

    train_data.drop('取引価格（総額）_log', axis=1, inplace=True)
    #データのない列を削除する
    for data in train_data.columns:
        if train_data[data].isnull().sum() == train_data.shape[0]:
            train_data.drop(data,axis=1, inplace=True)

    train_data.drop('ID',axis=1, inplace=True)
    train_data.drop('種類',axis=1, inplace=True)

    df = pd.concat([train_data,input_data],axis=0)
    df.reset_index(drop=True, inplace=True)

    df['面積（㎡）'] = df['面積（㎡）'].apply(lambda x:  area(x))
    df['最寄駅：距離（分）'] = df['最寄駅：距離（分）'].apply(lambda x: time(x))
    df['面積（㎡）'] = df['面積（㎡）'].apply(lambda x: area(x))
    df['建築年'] = df['建築年'].apply(lambda x: years(x))
    df['取引年'] = df['取引時点'].apply(lambda x: trade_year(x))
    df['取引月'] = df['取引時点'].apply(lambda x: trade_month(x))

    data = df['取引の事情等'].str.split('・')

    torihiki_1 = []
    torihiki_2 = []
    for i in range(data.shape[0]):
        if data[i] == data[i]:
            torihiki_1.append(data[i][0])
            if len(data[i]) == 2:
                torihiki_2.append(data[i][1])
            else:
                torihiki_2.append(np.nan)
        else:
            torihiki_1.append(np.nan)
            torihiki_2.append(np.nan)

    torihiki = pd.DataFrame({'取引の事情_1':torihiki_1, '取引の事情_2':torihiki_2})
    df = pd.concat([df,torihiki],axis=1)
    df.drop('取引の事情等', axis=1, inplace=True)

    df['敷地面積（㎡）'] = (df['面積（㎡）']/df['建ぺい率（％）']*100).round(2)
    df['延べ床面積（㎡）'] = (df['容積率（％）']*df['敷地面積（㎡）']/100).round(2)

    #階数を算出
    df['階数'] = (df['延べ床面積（㎡）']/df['面積（㎡）']).round(0)

    #用途と今後の利用目的の正誤関係
    change = []
    for i in range(df.shape[0]):
        if df['用途'][i] == df['今後の利用目的'][i]:
            change.append(1)
        else:
            change.append(0)

    changes = pd.DataFrame(change, columns=['利用目的の変更'])
    df = pd.concat([df, changes],axis=1)

    ido = []
    keido = []
    for name in df['都道府県名']:
        ido.append(angle(name)[0])
        keido.append(angle(name)[1])

    df_angle = pd.DataFrame(list(zip(ido, keido)), columns=['緯度','経度'])
    df = pd.concat([df,df_angle], axis=1)

    #ラベルエンコーダー
    la = LabelEncoder()
    df['都道府県名'] = la.fit_transform(df['都道府県名'])
    df['市区町村名'] = la.fit_transform(df['市区町村名'])
    df['地区名'] = la.fit_transform(df['地区名'])
    df['最寄駅：名称'] = la.fit_transform(df['最寄駅：名称'])
    df['間取り'] = la.fit_transform(df['間取り'])
    df['建物の構造'] = la.fit_transform(df['建物の構造'])
    df['用途'] = la.fit_transform(df['用途'])
    df['今後の利用目的'] = la.fit_transform(df['今後の利用目的'])
    df['都市計画'] = la.fit_transform(df['都市計画'])
    df['改装'] = la.fit_transform(df['改装'])
    df['取引の事情_1'] = la.fit_transform(df['取引の事情_1'])
    df['取引の事情_2'] = la.fit_transform(df['取引の事情_2'])
    df['取引時点'] = la.fit_transform(df['取引時点'])

    train = df[:train_data.shape[0]]
    test = df[train_data.shape[0]:]

    return train, test


