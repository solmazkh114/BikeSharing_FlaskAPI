from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
# BaseEstimator is the base class for all estimators in sklearn. It implements a fit method to learn from data.
# TransformerMixin is just an object that responds to fit, transform, and fit_transform. it is the mixin class for all transformers in sklearn.
# Only standard transformers such as MinMaxScaler, StandardScaler, LabelEncoder etc. are made available in sklearn but with the BaseEstimator and TransformerMixin, 
# we can create custom transformers to fit some data pre-processing needed

    
class Preprocess(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X=None, y=None):
        return self
        

    def transform(self, X=None):
        return self
    

class ExtractData(Preprocess):

    def transform(self, X = None):
        X['year'] = pd.DatetimeIndex(X['datetime']).year
        X['month'] = pd.DatetimeIndex(X['datetime']).month
        X['hour'] = pd.DatetimeIndex(X['datetime']).hour
        X['dayofweek'] = pd.DatetimeIndex(X['datetime']).day_name()
        return X

     
        
class DataType(Preprocess):
    categorical = ["season", "holiday", "workingday", "weather", "year", "month", "hour", "dayofweek"]

    def transform(self , X = None):
        d = {}
        for cat in self.categorical:
            d[cat]  = "category"
        X = X.astype(d)
        return X
    
#class Encoding(Preprocess):

    #def transform(self, X= None):
       # X = pd.get_dummies(X, columns=['weather', 'season', 'year', 'month', 'hour', 'dayofweek'])
        #return X
    
class Encoding(Preprocess): #the Encoding class has to have a fit method to ensure it creates the same set of columns for any input data. 

    def fit(self, X, y=None):
        self.columns = pd.get_dummies(X, columns=['weather', 'season', 'year', 'month', 'hour', 'dayofweek']).columns
        return self

    def transform(self, X=None):
        X = pd.get_dummies(X, columns=['weather', 'season', 'year', 'month', 'hour', 'dayofweek'])
        missing_cols = set(self.columns) - set(X.columns)
        for col in missing_cols:
            X[col] = 0
        return X[self.columns]

    
class Drop(Preprocess):
    
    def transform(self, X = None):
        try:
            X = X.drop(["casual", "registered", "atemp", "datetime","count"], axis =1)
        except:
            X = X.drop(["atemp", "datetime"], axis =1)
        return X