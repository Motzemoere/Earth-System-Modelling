# 🌍 Earth-System-Modelling -> Data

Daily time series for a single ERA5 grid cell in Germany, covering **2008-01-01 to 2018-12-31** (4018 days).

| File | Location (lon, lat) |
|------|---------------------|
| `Data_swbm_Germany.csv` | 8.125 °E, 48.125 °N |

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

