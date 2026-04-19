"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np

def generate_data(seed):
    """Generate synthetic temperature sensor data.

    Parameters
    ----------
    seed : int
        Seed for the random number generator.

    Returns
    -------
    sensor_a : ndarray of shape (200,)
        Temperature readings from Sensor A, normally distributed with mean 25°C and std 3°C.
    sensor_b : ndarray of shape (200,)
        Temperature readings from Sensor B, normally distributed with mean 27°C and std 4.5°C.
    timestamps : ndarray of shape (200,)
        Sorted timestamps uniformly distributed from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    n_readings = 200
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n_readings)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n_readings)
    timestamps = np.sort(rng.uniform(0.0, 10.0, size=n_readings))
    return sensor_a, sensor_b, timestamps