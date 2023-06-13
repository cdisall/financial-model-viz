import numpy as np
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='ENXK3STTGG2HHKJ5')


class DataImporter(object):

    def __init__(self):  
        pass

    def get_ndarray(self, dict):
        dates = list(dict.keys())
        data = list(dict.values())   
        columns = list(data[0].keys())
        res = np.empty((len(dates), len(columns)), dtype=object)
        for i, point in enumerate(data):
            for j, column in enumerate(columns[1:]):
                res[i, j] = float(point[column])
        res = np.insert(res, 0, dates, axis=1)
        return res

if __name__ == '__main__':
    data, meta_data = ts.get_intraday('GOOGL')
    d = DataImporter()
    print(d.get_ndarray(data)[:2])





