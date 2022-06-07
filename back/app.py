from flask import Flask
import json
from flask import request
import numpy as np
import pandas as pd
import joblib

# from livereload import Server

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
