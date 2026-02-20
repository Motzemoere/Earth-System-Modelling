# 🌍 Earth-System-Modelling

This repository contains the **simple water balance model (SWBM)** used in the **Earth System Modelling** course.  
It is designed to demonstrate the most basic version of the model.

---

## ✨ Features

- 🧹 Preprocessing of input data for the water balance model
- 💧 Simulation of **soil moisture**, **runoff**, and **evapotranspiration**
- ⏱ Easy-to-run time series simulations
- 📊 Correlation analysis between model output and observed data

---
## 🗂 Input Data

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
## ⚙️ Configuration

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
## 🚀 Getting Started on your Local Machine

Follow these steps to set up the environment and run the model.

### 1. Install Git

If you do not have Git installed on your system, download and install **Git** for your system:

🌐 [Git Downloads](https://git-scm.com/downloads)

### 2. Clone the Repository

```bash
git clone https://github.com/Motzemoere/Earth-System-Modelling.git
cd Earth-System-Modelling
```


### 4. Create and Activate an Environment
The easiest way is to use pip and a virtual environment:
```bash
# Install Python from https://www.python.org/downloads/ if not already installed
python -m venv esm
source esm/bin/activate  # on Windows: esm\Scripts\activate
pip install pandas numpy # install necessary packages
```

However I would recomend using conda:


#### Install Conda
If you do not have Conda installed, download and install **Miniforge** for your system:

🌐 [Miniforge Releases](https://github.com/conda-forge/miniforge/releases?after=4.10.3-0)

You should now have access to the Miniforge prompt command terminal

The easiest way is to just create the environment manually by runnning these commands in the miniforge prompt:
```bash
conda create -n esm python pandas numpy matplotlib -y
conda activate esm
```

### 4.  🏃Running the Model
Open the cloned repository folder in you prefered IDE, select the esm env as your Python interpreter and start playing around.

You can find a complete example workflow, including how to run the SWBM model, and compute correlations with observed data, in the following file:

➡️ [`swbm.py`](swbm.py)

There is also a R version of the model prvided:

➡️ [`swbm.r`](run_swbm.r)


---
### 📬 Contact

If you have any questions, feel free to reach out:

✉️ [mattis.pfenning@email.uni-freiburg.de](mailto:mattis.pfenning@email.uni-freiburg.de)


## Reference
Koster, R. D., and S. P. P. Mahanama, 2012: Land surface controls on hydroclimatic means and variability. J. Hydrometeor., 13, 1604 1620, doi:10.1175/JHM-D-12-050.1.


