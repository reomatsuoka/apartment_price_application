from django.shortcuts import render
from django.views.generic import View
from .forms import FeatureNameForm

import pandas as pd
import numpy as np
from catboost import Pool
from sklearn.preprocessing import StandardScaler
import pickle
from glob import glob

from .defs import *
from .preprocessing import application_preprocessing

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = FeatureNameForm(request.POST or None)

        return render(request, 'app/index.html', {
            'form': form,
        })

class AnserView(View):
    def get(self, request, *args, **kwargs):
        form = FeatureNameForm(request.POST or None)
        prefecture = request.GET['prefecture']
        city = request.GET['city']
        district = request.GET['district']
        station_name = request.GET['station_name']
        station_distance = request.GET['station_distance']
        floor_plan = request.GET['floor_plan']
        area = request.GET['area']
        age = request.GET['age']
        structure = request.GET['structure']
        use = request.GET['use']
        use_after = request.GET['use_after']
        city_planning = request.GET['city_planning']
        floor_area_ratio = request.GET['floor_area_ratio']
        volume = request.GET['volume']
        transaction = request.GET['transaction']
        reform = request.GET['reform']
        caution = request.GET['caution']

        params = {
            prefecture: prefecture,
            city: city,
            district: district,
            station_name: station_name,
            station_distance: station_distance,
            floor_plan : floor_plan,
            area: area,
            age: age,
            structure: structure,
            use: use,
            use_after: use_after,
            city_planning: city_planning,
            floor_area_ratio: floor_area_ratio,
            volume : volume,
            transaction: transaction,
            reform: reform,
            caution: caution,
        }
        
        result = list(params)
        input_data = pd.DataFrame({
            '都道府県名':[result[0]],
            '市区町村名':[result[1]],
            '地区名':[result[2]],
            '最寄駅：名称':[result[3]],
            '最寄駅：距離（分）':[result[4]],
            '間取り':[result[5]],
            '面積（㎡）':[result[6]],
            '建築年':[result[7]],
            '建物の構造':[result[8]],
            '用途':[result[9]],
            '今後の利用目的':[result[10]],
            '都市計画':[result[11]],
            '建ぺい率（％）':[result[12]],
            '容積率（％）':[result[13]],
            '取引時点':[result[14]],
            '改装':[result[15]],
            '取引の事情等':[result[16]]
        })
        train_data = []
        path = glob('data/train/*')
        for i in path:
            train = pd.read_csv(i)
            train_data.append(train)
        train_data = pd.concat(train_data)
        train_data.reset_index(drop=True, inplace=True)

        target = train_data[['取引価格（総額）_log']]
        scaler = StandardScaler()
        target = scaler.fit_transform(target)

        train, test = application_preprocessing(input_data, train_data)
        cat_model = pickle.load(open('catboost_model.pickle', 'rb'))
        test = Pool(test)
        pred_y = cat_model.predict(test)
        pred = np.expm1(scaler.inverse_transform([pred_y]))[0].round(2)



        return render(request, 'app/anser.html', {
                'pred': pred[0],
                'prefecture': result[0],
                'city': result[1],
                'district': result[2],
                'station_name': result[3],
                'station_distance': result[4],
                'floor_plan' : result[5],
                'area': result[6],
                'age': result[7],
                'structure': result[8],
                'use': result[9],
                'use_after': result[10],
                'city_planning': result[11],
                'floor_area_ratio': result[12],
                'volume' : result[13],
                'transaction': result[14],
                'reform': result[15],
                'caution': result[16],
            })
