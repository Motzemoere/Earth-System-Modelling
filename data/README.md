# Data

Three daily time-series datasets for single ERA5 grid cells, one per country. All files share the same structure and cover **2008-01-01 to 2018-12-31** (4018 days).

| File | Location (lon, lat) |
|------|---------------------|
| `Data_swbm_Germany.csv` | 8.125 °E, 48.125 °N |
| `Data_swbm_Spain.csv` | -3.625 °E, 38.625 °N |
| `Data_swbm_Sweden.csv` | 16.375 °E, 63.625 °N |

## Columns

| Column | Unit | Description |
|--------|------|-------------|
| `time` | — | Date (YYYY-MM-DD) |
| `longitude` / `latitude` | ° | Grid cell centre |
| `snr_[MJ/m2]` | MJ m⁻² | Net solar radiation |
| `tp_[mm]` | mm | Total precipitation |
| `ro_[m]` | m | Surface runoff |
| `sm_[m3/m3]` | m³ m⁻³ | Volumetric soil moisture (observed) |
| `le_[W/m2]` | W m⁻² | Latent heat flux |
| `t2m_[K]` | K | 2 m air temperature |
| `lai_[m2/m2]` | m² m⁻² | Leaf area index |
| `evi_[]` | — | Enhanced Vegetation Index |
| `ndvi_[]` | — | Normalised Difference Vegetation Index |

> **Note:** EVI and NDVI are `NaN` for the first 16 days of the Sweden dataset.

