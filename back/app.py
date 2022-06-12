from flask import Flask
import json
from flask import request
import numpy as np
import pandas as pd
import joblib
from jupyter.app import vk_full
from jupyter.app import ok_full
from jupyter.app import csv_full
from jupyter.app import tg_full
from jupyter.app import arrXY
from jupyter.app import series_arr


from data import classmatesData
from data import telegrammData
from data import vkData
from data import userData

# from livereload import Server

app = Flask(__name__)

def object_line(df, dfXName,dfYname,xKey,yKey, title, xType):
    data = arrXY(df, dfXName,dfYname,xKey,yKey)
    return{
            'component': 'LineCard',
            'title': title,
            'item': {
                'series': [{ 'data': data, 'yName': dfYname }],
                'xKey': xKey,
                'yKey': yKey,
                'xType': xType,
            }
            }

def object_points(df, dfXName,dfYname,xKey,yKey, title, xType):
    data = arrXY(df, dfXName,dfYname,xKey,yKey)
    return{
            'component': 'ScatterCard',
            'title': title,
            'item': {
                'series': [{ 'data': data, 'yName': dfYname }],
                'xKey': xKey,
                'yKey': yKey,
                'xType': xType,
            }
            }

def object_Pie(df, dfAngleName,dfLabelname,angleKey,labelKey, title):
    data = arrXY(df, dfAngleName,dfLabelname,angleKey,labelKey)
    return{
            'component': 'PieCard',
            'title': title,
            'item': {
              'data': data,
              'angleKey': angleKey,
              'labelKey': labelKey,
            }
          }


def object_histogram(df, dfXName,dfYname,xKey,yKey, title, xType):
    data = series_arr(df, dfXName,dfYname,xKey,yKey)

    return{
            'component': 'HistogramCard',
            'title': title,
            'item': {
              'series': data,
              'xKey': xKey,
              'yKey': yKey,
              'xType': xType,
            }
          }

@app.after_request
def set_response_headers(response):
    return response


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route('/api/compute', methods=['GET'])
def hello():
    clf = joblib.load('./jupyter/jupyter.pkl')

    args = request.args
    x1 = int(args.get('x1'))
    x2 = int(args.get('x2'))
    x3 = int(args.get('x3'))
    dataPd = pd.DataFrame(data={'x1': [x1], 'x2': [x2], 'x3': [x3]})
    answer = clf.predict(dataPd)
    # , cls=NumpyEncoder
    return json.dumps(int(answer[0]))


@app.route('/api/user', methods=['GET'])
def user():
    # data = userData()
    data_gender, data_city, dep_csv_birth_date = csv_full()

    return json.dumps([[
        object_Pie(data_city,'contract_sum','city','date','contract_sum','Сумма договора'),
        object_Pie(data_city,'purchase_sum','city','date','purchase_sum',' Покупки за месяц, сумма, руб'),
        object_Pie(data_city,'purchase_count','city','date','purchase_count','Покупки за месяц, кол-во'),
    ],
    [
        object_line(data_city,'city','contract_sum','date','city','Сумма договора','category'),
        object_line(data_city,'city','purchase_sum','date','city',' Покупки за месяц, сумма, руб','category')
    ],
    [
        object_points(dep_csv_birth_date,'birth_date','contract_sum','date','birth_date','Cумма договора','number'),
        object_points(dep_csv_birth_date,'birth_date','purchase_sum','date','birth_date','Покупки за месяц, сумма, руб','number'),
        object_points(dep_csv_birth_date,'birth_date','purchase_count','date','birth_date','Покупки за месяц, кол-во','number')
    ],
    [
        object_line(data_city,'city','purchase_count','date','city','Покупки за месяц, кол-во','category')
    ],
    [
        object_Pie(data_gender,'contract_sum','gender','date','contract_sum','Сумма договора'),
        object_Pie(data_gender,'purchase_sum','gender','date','purchase_sum',' Покупки за месяц, сумма, руб'),
        object_Pie(data_gender,'purchase_count','gender','date','purchase_count','Покупки за месяц, кол-во'),
    ]
    ]
    )

@app.route('/api/classmates', methods=['GET'])
def classmates():
    data, data_interval = ok_full()

    return json.dumps([[
        object_line(data,'datetime_post','likes','date','likes','Лайки','time'),
    ],
    [
        object_line(data,'datetime_post','comments','date','comments','Комментарии','time'),
        object_line(data,'datetime_post','reposts','date','reposts','Репосты','time'),
    ],
    [
        object_points(data_interval,'interval','likes','date','likes','Лайки','category'),
        object_points(data_interval,'interval','comments','date','comments','Комментарии','category'),
        object_points(data_interval,'interval','reposts','date','reposts','Репосты','category')
    ],
    [
        object_line(data,'datetime_post','coef_vov','date','coef_vov','Виральный охват','time')
    ]])


@app.route('/api/telegramm', methods=['GET'])
def telegramm():
    data, data_interval = tg_full()

    return json.dumps([[
        object_line(data,'datetime_post','views','date','views','Просмотры','time')
    ],
    [
        object_points(data_interval,'interval','coef_ohv','date','coef_ohv','Виральный охват','category'),
        object_points(data_interval,'interval','views','date','views','Просмотры','category'),
    ],
    [
        object_line(data,'datetime_post','coef_ohv','date','coef_ohv','Виральный охват','time'),
    ]])


@app.route('/api/vk', methods=['GET'])
def vk():
    data, data_interval = vk_full()

    return json.dumps([[
        object_line(data,'datetime_post','likes','date','likes','Лайки','time'),
        object_line(data,'datetime_post','views','date','views','Просмотры','time')
    ],
    [
        object_line(data,'datetime_post','comments','date','comments','Комментарии','time'),
        object_line(data,'datetime_post','reposts','date','reposts','Репосты','time'),
        object_line(data,'datetime_post','coef_ohv','date','coef_ohv','Коэффициент вовлеченности','time')
    ],
    [
        object_points(data_interval,'interval','likes','date','likes','Лайки','category'),
        object_points(data_interval,'interval','comments','date','comments','Комментарии','category'),
        object_points(data_interval,'interval','views','date','views','Просмотры','category'),
        object_points(data_interval,'interval','reposts','date','reposts','Репосты','category')
    ],
    [
        object_line(data,'datetime_post','coef_vov','date','coef_vov','Виральный охват','time')
    ]])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
