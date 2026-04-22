# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational Earth System Modelling project centered on a **Soil Water Balance Model (SWBM)**. The repository serves as a teaching environment, guiding students from Python basics through implementing a real environmental model.

## Running the Model

**Setup (Conda recommended):**
```bash
conda create -n esm python pandas numpy matplotlib -y
conda activate esm
```

**Run Python model:**
```bash
python swbm.py
```

**Run R model:** Source `swbm.R` in an R session (requires `dplyr`, `lubridate`).

**Run tutorials:** Launch Jupyter and open notebooks in `tutorials/` sequentially.

## Architecture

### Core Model (`swbm.py` / `swbm.R`)

The SWBM simulates daily soil moisture evolution. Both language implementations are functionally identical:

- **`prepro(raw_data)`** — Unit conversion (runoff m→mm, radiation MJ/m²→mm via latent heat constant, latent heat W/m²→mm)
- **`et_fraction(b0, w_i, c_s, g)`** — ET fraction: `b0 × (w_i / c_s)^g`
- **`runoff_fraction(w_i, c_s, a)`** — Runoff fraction: `min((w_i / c_s)^a, 1)`
- **`predict_sm(...)`** — Single timestep update: `w_{t+1} = w_t + tp - et×snr - ro×tp`
- **`predict_ts(data, config, n_days)`** — Main simulation loop; returns time series of ET, runoff, and soil moisture
- **`model_correlation(data, model_outputs, start, end)`** — Evaluates model against observations

**Model parameters** (configured as a dict in the main block):
| Parameter | Default | Meaning |
|-----------|---------|---------|
| `c_s` | 420 | Soil water holding capacity (mm) |
| `a` | 4 | Runoff shape parameter (α) |
| `g` | 0.5 | ET shape parameter (γ) |
| `b0` | 0.8 | ET maximum (β) |

### Data (`data/`)

Three country CSV datasets (Germany, Spain, Sweden). Key columns after preprocessing:
- `snr` — net solar radiation (mm equivalent)
- `tp` — precipitation (mm)
- `ro` — runoff (mm)
- `sm` — observed soil moisture (m³/m³)
- `le` — latent heat flux (mm equivalent)

The main script currently hardcodes `Data_swbm_Sweden.csv` as the input.

### Tutorials (`tutorials/`)

Five sequential Jupyter notebooks building from Python basics to SWBM:
1. Python basics and data structures
2. Pandas/NumPy for data analysis
3. Functions, loops, control flow
4. **Building a model** (plant growth model — directly mirrors SWBM structure)
5. Advanced Python (optimization, OOP, statistical analysis)

Notebook 4 is the direct pedagogical precursor to `swbm.py`.
