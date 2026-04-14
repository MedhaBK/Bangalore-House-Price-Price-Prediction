import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __data_columns[3:]

import os

import os

def load_saved_artifacts():
    print('loading stored artifacts...start')

    global __data_columns
    global __locations
    global __model

    base_path = os.path.dirname(os.path.abspath(__file__))

    # Load columns
    with open(os.path.join(base_path, "artifacts", "columns.json"), 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    # Load model
    with open(os.path.join(base_path, "artifacts", "bangalore_house_pries_model.pickle"), 'rb') as f:
        __model = pickle.load(f)

    print('loading saved artifacts...done')

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3,))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
