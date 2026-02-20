# ==========================
# Section 1: Import Libraries
# ==========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Section 2: Define Functions
# ==========================
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

def et_fraction(b0, w_i, c_s, g):
    """Compute proportion of maximum ET that occurs given current soil moisture."""
    w_i = np.minimum(w_i, c_s)  # soil moisture cannot exceed water holding capacity
    return b0 * (w_i / c_s) ** g

def runoff_fraction(w_i, c_s, a):
    """Compute runoff fraction."""
    return np.minimum((w_i / c_s) ** a, 1)

def predict_sm(curr_moist, evapo, wrunoff, precip, rad):
    """Update soil moisture for next step."""
    return curr_moist + (precip - (evapo * rad) - (wrunoff * precip))

def predict_ts(data, config, n_days=None):
    """Run the SWBM for given time series

    :param data: input data (pandas df) (time, tp, sm, ro, le, snr)
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
    moists, runoff_fracs, et_fracs = np.zeros(n_days), np.zeros(n_days), np.zeros(n_days)

    # Initial soil moisture (90% of soil water holding capacity)
    moists[0] = 0.9 * config['c_s']
    
    # Parameters
    c_s = config['c_s']
    b0 = config['b0']
    g = config['g']
    a = config['a']

    for i in range(n_days):
        # Compute evapotranspiration fraction
        # what fraction of the available energy can actually drive evaporation right now?
        et_fracs[i] = et_fraction(b0, moists[i], c_s, g)

        # Compute runoff fraction
        # what fraction of incoming rainfall will run off rather than soak in?
        runoff_fracs[i] = runoff_fraction(moists[i], c_s, a)

        # Compute soil moisture for the next timestep
        if i < n_days - 1: # Avoid updating beyond the last index
            moists[i + 1] = predict_sm(moists[i], et_fracs[i], runoff_fracs[i],
                                    data['tp'][i], data['snr'][i])

    # Convert runoff and ET fractions to actual fluxes
    runoffs = runoff_fracs * np.asarray(data['tp']) # fraction × precipitation
    ets = et_fracs * np.asarray(data['snr']) # fraction × net solar radiation

    return moists, runoffs, ets

def model_correlation(data, model_outputs, start=None, end=None):
    """
    Calculate correlation between observed data and model outputs,
    optionally restricted to a timeframe.

    :param data: pandas DataFrame with columns 'sm', 'ro', 'le' (observed)
    :param model_outputs: tuple of numpy arrays (moists, runoffs, ets)
    :param start: str or datetime, start date for analysis (optional)
    :param end: str or datetime, end date for analysis (optional)
    :return: dict with individual correlations and sum of correlations
    """
    moists, runoffs, ets = model_outputs

    # Apply timeframe selection if provided
    if start is not None or end is not None:
        mask = (data['time'] >= pd.to_datetime(start) if start else True) & \
               (data['time'] <= pd.to_datetime(end) if end else True)
        data = data.loc[mask]
        moists = moists[data.index]
        runoffs = runoffs[data.index]
        ets = ets[data.index]

    # Compute correlations
    corr_sm = np.corrcoef(data['sm'], moists)[0, 1]
    corr_ro = np.corrcoef(data['ro'], runoffs)[0, 1]
    corr_et = np.corrcoef(data['le'], ets)[0, 1]

    corr_sum = corr_sm + corr_ro + corr_et

    return {'sm': corr_sm, 'ro': corr_ro, 'et': corr_et, 'sum': corr_sum}

# ==========================
# Section 3: Main Execution
# ==========================

# Define path to data file
data = pd.read_csv("data/Data_swbm_Sweden_old.csv")

# Prepare the data
data_prepro = prepro(data)

# Define initial parameters
config = {
    'c_s': 420,    # soil water holding capacity in mm
    'a': 4,        # runoff function shape α
    'g': 0.5,      # ET function shape γ
    'b0': 0.8      # maximum of ET function β
}

# Run the SWBM model
moisture, runoff, et_flux = predict_ts(data_prepro, config)

# Compute correlation over the whole timeseries
corrs = model_correlation(data_prepro, (moisture, runoff, et_flux))
print("Correlation between observed data and model outputs:\n")
print(f"Soil Moisture (sm):    {corrs['sm']:.3f}")
print(f"Runoff (ro):           {corrs['ro']:.3f}")
print(f"Evapotranspiration (et): {corrs['et']:.3f}")
print(f"\nSum of correlations:   {corrs['sum']:.3f}")
