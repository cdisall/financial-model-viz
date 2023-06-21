"""""
Main method to run local tests
"""
import DataImporter
import Predictor
import numpy as np
import datetime

if __name__ == '__main__':
    # Create data importer and predictor
    di = DataImporter.DataImporter()
    predictor = Predictor.Predictor()
    # Get last 252 days of data for GOOGL
    data = di.get_close_data(('GOOGL'))
    #Generate next 50 dates
    start_date = datetime.datetime.strptime(data[0,0], "%Y-%m-%d").date()
    print(start_date)
    dates = np.array([start_date + datetime.timedelta(days=i) for i in range(50)])
    print(dates[:4])