"""Time series forecasting for FRED economic data."""

__version__ = "0.1.0"

from .calibration import calibrate_simulations

# Import user-facing classes and functions
from .data import fetch_fred_data, get_series_name, get_series_title
from .models.bayesian import fit_bayesian_model, generate_bayesian_simulations
from .models.sarimax import fit_sarimax_model, generate_simulations
from .visualization import plot_drop_probabilities, plot_forecasts
