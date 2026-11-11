# 🌍 Earth-System-Modelling -> Model

Here you find the most basic version of the Simple Water Balance Model (SWBM):

**First time here?** I recommend starting with the [Python Tutorials](../tutorials/README.md) if you're new to programming. They'll teach you everything you need to understand this model.

**Already familiar with Python?** You can find a complete example workflow for running the SWBM model in:

➡️ [`swbm.py`](swbm.py) — or as a notebook for Colab: [`swbm.ipynb`](swbm.ipynb)

There is also an R version of the model provided:

➡️ [`swbm.R`](swbm.R)

Both scripts load the data directly from GitHub via `DATA_URL`, so they also run in Google Colab. To work offline, point `DATA_URL` to your local `data/` folder.

---

## Features

- 🧹 Preprocessing of input data for the water balance model
- 💧 Simulation of **soil moisture**, **runoff**, and **evapotranspiration**
- ⏱ Easy-to-run time series simulations
- 📊 Correlation analysis between model output and observed data

---
## Input Data

The model requires an input CSV file with the following variables:

📅 time: Date or timestamp

🌐 latitude and longitude

☔ tp_[mm]: Precipitation in mm

☀️ snr_[MJ/m2]: Surface net radiation

Optional: (used for correlation with observations):

🌱 sm_[m3/m3]: Soil moisture

🌊 ro_[m]: Runoff

🔥 le_[W/m2]: Latent heat flux

---
## Configuration

The model uses a configuration dictionary with these example parameters:

| Parameter | Description                      | Example |
| --------- | -------------------------------- | ------- |
| `c_s`     | Soil water holding capacity (mm) | 420     |
| `a`       | Runoff function shape (α)        | 4       |
| `g`       | ET function shape (γ)            | 0.5     |
| `b0`      | Maximum of ET function (β)       | 0.8     |

Python example:

```python
config = {
    'c_s': 420,
    'a': 4,
    'g': 0.5,
    'b0': 0.8
}
```

---
## How the Model Works

Each box is a function; `predict_ts` calls the three inner functions once per day.

```mermaid
flowchart TD
    csv[("Input CSV<br/>e.g. Data_swbm_Germany.csv")] --> prepro
    prepro["<b>prepro</b><br/>unit conversion to mm<br/>tp, snr, sm, ro, le"] --> predict_ts
    config[/"<b>config</b><br/>c_s, a, g, b0"/] --> predict_ts

    subgraph predict_ts["<b>predict_ts</b> — loop over days, start: W = 0.9 · c_s"]
        direction TB
        W(("soil moisture W<sub>t</sub>")) --> et_fraction["<b>et_fraction</b><br/>b0 · (W/c_s)<sup>g</sup>"]
        W --> runoff_fraction["<b>runoff_fraction</b><br/>(W/c_s)<sup>a</sup>"]
        et_fraction --> predict_sm
        runoff_fraction --> predict_sm
        predict_sm["<b>predict_sm</b><br/>W<sub>t+1</sub> = W<sub>t</sub> + P − ET − Q"] -->|next day| W
    end

    predict_ts --> out[/"model output<br/>soil moisture, runoff Q, ET"/]
    out --> model_correlation["<b>model_correlation</b><br/>correlation with observed sm, ro, le"]
    prepro -. observations .-> model_correlation
```

Daily water balance, with precipitation $P$ and net radiation $R_n$ (both in mm):

$$W_{t+1} = W_t + P_t - \underbrace{\beta_0 \left(\tfrac{W_t}{c_s}\right)^{\gamma} R_{n,t}}_{ET_t} - \underbrace{\left(\tfrac{W_t}{c_s}\right)^{\alpha} P_t}_{Q_t}$$
