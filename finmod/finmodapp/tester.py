"""""
Main method to run local tests
"""
import DataImporter
import Predictor
import numpy as np
import datetime

if __name__ == '__main__':

    ####################### COPY AND PASTE EVERYTHIGN BELOW THIS LINE ############################################
    # Create data importer and predictor
    di = DataImporter.DataImporter()
    predictor = Predictor.Predictor()
    # Get last 252 days of data for GOOGL
    """
    Save text as locally for testing to save api pulls

    data = di.get_close_data(('GOOGL'))
    np.savetxt("GOOGL.csv", data, delimiter=",",fmt="%s")
    """
    # Import from locally saved file
    dtype = np.dtype([('Date', 'U10'), ('Close Price', float)])
    data = np.genfromtxt('GOOGL.csv', delimiter=",", dtype=dtype, skip_header=1)
    data = np.array([list(d) for d in data])

    #Generate next 50 dates
    start_date = datetime.datetime.strptime(data[0,0], "%Y-%m-%d").date()
    # Weekends and holidays not included yet
    dates = np.array([start_date + datetime.timedelta(days=i) for i in range(50)])
    data = np.array([list(d) for d in data])

    # Prepare data
    dates = data[:, 0]
    prices = data[:, 1].astype(float)
    # Convert string dates to datetime objects
    dates = np.array([datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates])
    # Convert dates to timestamps
    timestamps = np.array([date.timestamp() for date in dates])
    # Separate to X, y
    X = timestamps.reshape(-1, 1) 
    y = prices  

    # Train predictor
    predictor.train(X, y)

    # Get the next 50 dates
    next_dates = [dates[-1] + datetime.timedelta(days=i) for i in range(1, 51)]
    # Convert next 50 dates to timestamps
    next_timestamps = np.array([date.timestamp() for date in next_dates])
    # PReshape to a 2D array
    X_pred = next_timestamps.reshape(-1, 1)

    # Predict next 50 close prices
    preds = predictor.query(X_pred)

    # Create ndarray with preds
    pred_data = np.column_stack((next_dates, preds))
    print(pred_data[:,1])
