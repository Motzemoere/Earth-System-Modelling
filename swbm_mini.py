import pandas as pd
import numpy as np

def prepro(raw_data):
    """ Preprocess data for SWBM
    Convert runoff, latent heat flux and solar net radiation to mm.
    Convert time to date.

    :param raw_data: raw input data (pandas df):
         -snr: surface net radiation
         -tp: total precipitation
         -ro: runoff
         -sm: soil moisture at the surface
         -le: latent heat flux
    :return: pre-processed data (pandas df)
    """

    data = {'time': pd.to_datetime(raw_data['time']),
            'lat': raw_data['latitude'],
            'long': raw_data['longitude'],
            'tp': raw_data['tp_[mm]'],
            'sm': raw_data['sm_[m3/m3]'] * 1000,
            'ro': raw_data['ro_[m]'] * 24000,
            'le': raw_data['le_[W/m2]'] * (86400 / 2260000),
            # 86400 (seconds) / 2260000 (latent heat of vaporization
            # of water in J/kg)
            'snr': raw_data['snr_[MJ/m2]'] * (1 / 2.26),
            }

    return pd.DataFrame(data)

def et(b0, w_i, c_s, g):
    return b0 * (w_i / c_s) ** g

def runoff(w_i, c_s, a):
    return (w_i / c_s) ** a

def predict(curr_moist, evapo, wrunoff, precip, rad):
    return curr_moist + (precip - (evapo * rad) - (wrunoff * precip))
