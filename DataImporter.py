import numpy as np
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='ENXK3STTGG2HHKJ5')


class DataImporter(object):

    def __init__(self):  
        pass

    def get_ndarray(self, dict):
        """  		  	   		  		 			  		 			 	 	 		 		 	
        Convert stock data to ndarray		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
        :param dict: Dictionary with keys as dates in form 
            '2023-06-12': {'1. open': '122.785', '2. high': '124.05', '3. low': '121.66', '4. close': '123.64', '5. adjusted close': '123.64', '6. volume': '28338743', '7. dividend amount': '0.0000', '8. split coefficient': '1.0'}
        :type dict: dict  		  	   		  		 			  		 			 	 	 		 		 	
        :output res: 2D ndarray where each row represents a date from dict   		  	   		  		 			  		 			 	 	 		 		 	
        :type res: numpy.ndarray  		  	   		  		 			  		 			 	 	 		 		 	
        """  
        dates = list(dict.keys())
        data = list(dict.values())   
        columns = list(data[0].keys())
        res = np.empty((len(dates), len(columns)), dtype=object)
        for i, point in enumerate(data):
            for j, column in enumerate(columns[1:]):
                res[i, j] = float(point[column])
        res = np.insert(res, 0, dates, axis=1)
        return res
    
    def get_data(self, sym):
         """  		  	   		  		 			  		 			 	 	 		 		 	
           Get data for stock with ticker symbol sym		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
        :param sym: Ticker symbol
        :type sym: str		  	   		  		 			  		 			 	 	 		 		 	
        :output self.get_ndarray(data): 2D ndarray where each row represents stock data for the sym for one day (adjusted) 		  	   		  		 			  		 			 	 	 		 		 	
        :type self.get_ndarray(data): numpy.ndarray  		  	   		  		 			  		 			 	 	 		 		 	
        """  
        data, meta = ts.get_daily_adjusted(sym)
        return self.get_ndarray(data)

if __name__ == '__main__':
    d = DataImporter()
    sym = 'GOOGL'
    print(d.get_data(sym)[:4])





