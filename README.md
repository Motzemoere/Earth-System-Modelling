# 🌍 Earth-System-Modelling

This repository contains a **simple water balance model (SWBM)** used in the **Earth System Modelling** course.  
It is designed to demonstrate the most basic version of the model.

---

## ✨ Features

- 🧹 Preprocessing of input data for the water balance model
- 💧 Simulation of **soil moisture**, **runoff**, and **evapotranspiration**
- ⏱ Easy-to-run time series simulations
- 📈 Plotting of results
- 📊 Correlation analysis between model output and observed data

---

## 🚀 Getting Started

Follow these steps to set up the environment and run the model.

### 1. Clone the Repository

```bash
git clone https://github.com/<your-repo>/Earth-System-Modelling.git
cd Earth-System-Modelling
```

### 2. Install Conda

If you do not have Conda installed, download **Miniforge**:

[Miniforge Releases](https://github.com/conda-forge/miniforge/releases?after=4.10.3-0)

### 3. Create and Activate the Environment

Use the provided `environment.yml` file to create a Python environment with all dependencies:

```bash
cd Earth-System-Modelling
conda env create -f environment.yml
conda activate esm
```

🗂 Input Data

The model requires an input CSV file with the following variables:

📅 time: Date or timestamp
🌐 latitude and longitude
☔ tp_[mm]: Precipitation in mm
🌱 sm_[m3/m3]: Soil moisture
🌊 ro_[m]: Runoff
🔥 le_[W/m2]: Latent heat flux
☀️ snr_[MJ/m2]: Surface net radiation

An example file is provided in the data/ folder:
📊 [`Data_swbm_Germany.csv`](data/Data_swbm_Germany.csv)

### ⚙️ Configuration

The model uses a configuration dictionary with these parameters:

| Parameter | Description                      | Example |
| --------- | -------------------------------- | ------- |
| `c_s`     | Soil water holding capacity (mm) | 420     |
| `a`       | Runoff function shape (α)        | 4       |
| `g`       | ET function shape (γ)            | 0.5     |
| `b0`      | Maximum of ET function (β)       | 0.8     |

Example:

```python
config = {
    'c_s': 420,
    'a': 4,
    'g': 0.5,
    'b0': 0.8
}
```

###  🏃Running the Model

You can find a complete example workflow, including how to run the SWBM model, plot the results, and compute correlations with observed data, in the following file:

➡️ [`run_swbm.py`](run_swbm.py)


