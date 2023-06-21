import xgboost as xgb

class Predictor(object):

    def __init__(self, model = 'xbg'):  
        self.model_name = model
        self.model = xgb.XGBRegressor()

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def query(self, x_test):
        return self.model.predict(x_test)