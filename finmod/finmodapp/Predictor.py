import xgboost as xgb

class Predictor(object):

    def __init__(self, model = 'xbg'):  
        self.model = model

    def train(self, x_train, y_train):
        if self.model == 'xgb':
            self.model = xgb.XGBRegressor()
        self.model.fit(x_train, y_train)

    def query(self, x_test):
        return self.model(x_test)