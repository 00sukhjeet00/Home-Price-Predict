import pickle
import json
import numpy as np
__location=None
__data_columns=None
__model=None
def get_price(location,sqft,bhk,bath):
    global __data_columns
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)
def get_locations():
    global __location
    return __location
def load_saved_location():
    global __location
    global __data_columns
    global __model
    with open('./model/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']
        __location=__data_columns[3:]
    with open('./model/bengalore_pickle','rb') as f:
        __model=pickle.load(f)
if __name__ == '__main__':
    load_saved_location()