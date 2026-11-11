# 🌍 Earth-System-Modelling -> Data

Daily time series for three ERA5 grid cells, each covering **2008-01-01 to 2018-12-31** (4018 days). All files share the same columns.

| File | Location (lon, lat) |
|------|---------------------|
| `Data_swbm_Germany.csv` | 8.125 °E, 48.125 °N |
| `Data_swbm_Spain.csv` | 3.625 °W, 38.625 °N |
| `Data_swbm_Sweden.csv` | 16.375 °E, 63.625 °N |

## Columns

| Column | Unit | Description |
|--------|------|-------------|
| `time` | — | Date (YYYY-MM-DD) |
| `longitude` / `latitude` | ° | Grid cell centre |
| `snr_[MJ/m2]` | MJ m⁻² | Surface net radiation (shortwave + longwave, daily sum; negative when the surface loses more energy than it receives) |
| `tp_[mm]` | mm | Total precipitation |
| `ro_[m]` | m | Surface runoff |
| `sm_[m3/m3]` | m³ m⁻³ | Volumetric soil moisture (observed) |
| `le_[W/m2]` | W m⁻² | Latent heat flux |
| `t2m_[K]` | K | 2 m air temperature |
| `lai_[m2/m2]` | m² m⁻² | Leaf area index |
| `evi_[]` | — | Enhanced Vegetation Index |
| `ndvi_[]` | — | Normalised Difference Vegetation Index |

