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

def predict_ts(data, config, n_days=None):
    """Run the SMBW for given time series

    :param data: input data (pandas df) (time, lat, long, tp, sm, ro, le, snr)
    :param config: parameters
                   - water holding capacity (c_s),
                   - maximum of ET function (b0),
                   - ET function shape (g),
                   - runoff function shape (a))
    :param n_days: time series length (default: None)
    :return: soil moisture, runoff, ET (for entire ts) (numpy arrays)
    """
    n_days = data.shape[0] if n_days is None else n_days

    # Initialize arrays for model outputs
    moists, runoffs, ets = np.zeros(n_days), np.zeros(n_days), np.zeros(n_days)
    curr = {}  # to temporarily store parameters in loop

    # Initial soil moisture (90% of soil water holding capacity)
    moists[0] = 0.9 * config['c_s']
    
    # Parameters
    c_s = config['c_s']
    b0 = config['b0']
    g = config['g']
    a = config['a']

    for i in range(n_days):

        # Compute evapotrans. and runoff
        ets[i] = et(b0, moists[i], c_s, g)
        runoffs[i] = runoff(moists[i], c_s, a)

        # Compute soil moisture
        if i < n_days - 1:
            moists[i + 1] = predict(moists[i], ets[i], runoffs[i],
                                    data['tp'][i], data['snr'][i])

    return moists, runoffs * np.asarray(data['tp']), ets * np.asarray(data['snr'])

def model_correlation(data, model_outputs):
    """
    Calculate correlation between observed data and model outputs.

    :param data: pandas DataFrame with columns 'sm', 'ro', 'le' (observed)
    :param model_outputs: tuple of numpy arrays (moists, runoffs, ets)
    :return: dict with individual correlations and sum of correlations
    """
    moists, runoffs, ets = model_outputs
    
    corr_sm = np.corrcoef(data['sm'], moists)[0, 1]
    corr_ro = np.corrcoef(data['ro'], runoffs)[0, 1]
    corr_et = np.corrcoef(data['le'], ets)[0, 1]
    
    corr_sum = corr_sm + corr_ro + corr_et
    
    return {'sm': corr_sm, 'ro': corr_ro, 'et': corr_et, 'sum': corr_sum}
