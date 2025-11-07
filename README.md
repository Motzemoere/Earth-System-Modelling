# 🌍 Earth-System-Modelling

This repository contains the **simple water balance model (SWBM)** used in the **Earth System Modelling** course.  
It is designed to demonstrate the most basic version of the model.

---

## ✨ Features

- 🧹 Preprocessing of input data for the water balance model
- 💧 Simulation of **soil moisture**, **runoff**, and **evapotranspiration**
- ⏱ Easy-to-run time series simulations
- 📈 Plotting of results
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



An example file is provided in the data/ folder:
📊 [`Data_swbm_Germany.csv`](data/Data_swbm_Germany.csv)

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

## 🚀 Getting Started on your Local Machine

Follow these steps to set up the environment and run the model.

### 0. Install Git

If you do not have Git installed on your system, download and install **Git** for your system:

🌐 [Git Downloads](https://git-scm.com/downloads)

### 1. Clone the Repository

```bash
git clone https://github.com/Motzemoere/Earth-System-Modelling.git
cd Earth-System-Modelling
```

### 2. Install Conda

If you do not have Conda installed, download and install **Miniforge** for your system:

🌐 [Miniforge Releases](https://github.com/conda-forge/miniforge/releases?after=4.10.3-0)

You should now have access to the Miniforge Prombt command terminal

### 3. Create and Activate the Environment

The easiest way is to just create the environment manually by runnning these commands in the miniforge prompt:
```bash
conda create -n esm python pandas numpy matplotlib -y
conda activate esm
```
Alternatively:

Use the provided `environment.yml` file to create a Python environment with all dependencies in one go:
(this is how its normally done with bigger envs)

Run and confirm this in your miniforge prompt:
```bash
cd Earth-System-Modelling
conda env create -f environment.yml
conda activate esm
```



###  🏃Running the Model

You can find a complete example workflow, including how to run the SWBM model, plot the results, and compute correlations with observed data, in the following file:

➡️ [`run_swbm.py`](run_swbm.py)

## 🚀 Getting Started on Google Colab
### 1. Open a new Notebook in Google Colab
### 2. Mount your Google Drive: (run this commands in a new code cell)
```python
from google.colab import drive
drive.mount('/content/drive')
# Follow the instruction to allow access to your google drive
```

### 3. Clone the Repository into your Google Drive
Open up a Terminal in Google Colab  (bottom left corner) and run the following commands:
```bash
cd drive/MyDrive
git clone https://github.com/Motzemoere/Earth-System-Modelling.git
cd Earth-System-Modelling
```
Alternatively you could also just clone the repository to your local machine (see above) and then upload it to Google Drive.

### 4. Run the SWBM
In the repository, there is a complete example flow for running the SWBM: [`run_swbm_colab.ipynb`](run_swbm_colab.ipynb).
However, to open the script in Colab, you need to go back to **Google Drive**, navigate to the GitHub repository that you just cloned, and open the script from there using the 'Open with' option, selecting Google Colaboratory.

### 📬 Contact

If you have any questions, feel free to reach out:

✉️ [mattis.pfenning@email.uni-freiburg.de](mailto:mattis.pfenning@email.uni-freiburg.de)


## Reference
Koster, R. D., and S. P. P. Mahanama, 2012: Land surface controls on hydroclimatic means and variability. J. Hydrometeor., 13, 1604 1620, doi:10.1175/JHM-D-12-050.1.


