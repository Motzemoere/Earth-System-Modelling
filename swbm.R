# ==========================
# Section 1: Load Libraries
# ==========================
library(dplyr)
library(lubridate)

# ==========================
# Section 2: Define Functions
# ==========================

prepro <- function(raw_data) {
  #' Preprocess data for SWBM
  #' Convert runoff, latent heat flux and solar net radiation to mm.
  #' Convert time to date.
  #'
  #' @param raw_data raw input data (data.frame):
  #'   - snr: surface net radiation
  #'   - tp:  total precipitation
  #'   - ro:  runoff
  #'   - sm:  soil moisture at the surface
  #'   - le:  latent heat flux
  #' @return pre-processed data (data.frame)

  data.frame(
    time = as.POSIXct(raw_data$time),
    lat  = raw_data$latitude,
    long = raw_data$longitude,
    tp   = raw_data$`tp_[mm]`,
    sm   = raw_data$`sm_[m3/m3]` * 1000,
    ro   = raw_data$`ro_[m]`     * 24000,
    le   = raw_data$`le_[W/m2]`  * (86400 / 2260000),
    # 86400 (seconds) / 2260000 (latent heat of vaporization of water in J/kg)
    snr  = raw_data$`snr_[MJ/m2]` * (1 / 2.26)
  )
}


et_fraction <- function(b0, w_i, c_s, g) {
  #' Compute proportion of maximum ET that occurs given current soil moisture.
  #' Result is a value between 0 and b0.
  w_i <- pmin(w_i, c_s)  # soil moisture cannot exceed water holding capacity
  b0 * (w_i / c_s) ^ g
}


runoff_fraction <- function(w_i, c_s, a) {
  #' Compute runoff fraction.
  #' Result is capped at 1 (can't have more than 100% runoff).
  pmin((w_i / c_s) ^ a, 1)
}


predict_sm <- function(curr_moist, evapo, wrunoff, precip, rad) {
  #' Update soil moisture for next timestep.
  curr_moist + (precip - (evapo * rad) - (wrunoff * precip))
}


predict_ts <- function(data, config, n_days = NULL) {
  #' Run the SWBM for a given time series.
  #'
  #' @param data   input data (data.frame) with columns: time, tp, sm, ro, le, snr
  #' @param config named list of parameters:
  #'               - c_s: water holding capacity (mm)
  #'               - b0:  maximum of ET function
  #'               - g:   ET function shape (gamma)
  #'               - a:   runoff function shape (alpha)
  #' @param n_days time series length (default: NULL = use all rows)
  #' @return list with soil moisture, runoff, and ET (numeric vectors)

  if (is.null(n_days)) n_days <- nrow(data)

  # Initialize arrays for model outputs
  moists       <- numeric(n_days)
  et_fracs     <- numeric(n_days)
  runoff_fracs <- numeric(n_days)

  # Initial soil moisture (90% of soil water holding capacity)
  moists[1] <- 0.9 * config$c_s

  # Unpack parameters for convenience
  c_s <- config$c_s
  b0  <- config$b0
  g   <- config$g
  a   <- config$a

  for (i in seq_len(n_days)) {

    # Compute evapotranspiration fraction
    # what fraction of the available energy can actually drive evaporation right now?
    et_fracs[i] <- et_fraction(b0, moists[i], c_s, g)

    # Compute runoff fraction
    # what fraction of incoming rainfall will run off rather than soak in?
    runoff_fracs[i] <- runoff_fraction(moists[i], c_s, a)

    # Compute soil moisture for the next timestep
    if (i < n_days) {  # Avoid updating beyond the last index
      moists[i + 1] <- predict_sm(
        moists[i], et_fracs[i], runoff_fracs[i],
        data$tp[i], data$snr[i]
      )
    }
  }

  # Convert runoff and ET fractions to actual fluxes
  runoffs <- runoff_fracs * data$tp   # fraction x precipitation
  ets     <- et_fracs     * data$snr  # fraction x net solar radiation

  list(moists = moists, runoffs = runoffs, ets = ets)
}


model_correlation <- function(data, model_outputs, start = NULL, end = NULL) {
  #' Calculate correlation between observed data and model outputs,
  #' optionally restricted to a timeframe.
  #'
  #' @param data          data.frame with observed columns: sm, ro, le
  #' @param model_outputs list with moists, runoffs, ets (numeric vectors)
  #' @param start         start date for analysis (optional, character or POSIXct)
  #' @param end           end date for analysis (optional, character or POSIXct)
  #' @return named list with individual correlations and their sum

  moists  <- model_outputs$moists
  runoffs <- model_outputs$runoffs
  ets     <- model_outputs$ets

  # Apply timeframe selection if provided
  if (!is.null(start) || !is.null(end)) {
    mask <- rep(TRUE, nrow(data))
    if (!is.null(start)) mask <- mask & (data$time >= as.POSIXct(start))
    if (!is.null(end))   mask <- mask & (data$time <= as.POSIXct(end))

    data    <- data[mask, ]
    moists  <- moists[mask]
    runoffs <- runoffs[mask]
    ets     <- ets[mask]
  }

  # Compute correlations between observed and modelled variables
  corr_sm <- cor(data$sm, moists)
  corr_ro <- cor(data$ro, runoffs)
  corr_et <- cor(data$le, ets)

  list(
    sm  = corr_sm,
    ro  = corr_ro,
    et  = corr_et,
    sum = corr_sm + corr_ro + corr_et
  )
}

# ==========================
# Section 3: Main Execution
# ==========================

# Load data
data <- read.csv("data/Data_swbm_Sweden_old.csv")

# Prepare the data
data_prepro <- prepro(data)

# Define initial parameters
config <- list(
  c_s = 420,   # soil water holding capacity in mm
  a   = 4,     # runoff function shape alpha
  g   = 0.5,   # ET function shape gamma
  b0  = 0.8    # maximum of ET function beta
)

# Run the SWBM model
outputs <- predict_ts(data_prepro, config)

# Compute correlation over the whole timeseries
corrs <- model_correlation(data_prepro, outputs)

cat("Correlation between observed data and model outputs:\n\n")
cat(sprintf("Soil Moisture (sm):      %.3f\n", corrs$sm))
cat(sprintf("Runoff (ro):             %.3f\n", corrs$ro))
cat(sprintf("Evapotranspiration (et): %.3f\n", corrs$et))
cat(sprintf("\nSum of correlations:     %.3f\n", corrs$sum))
