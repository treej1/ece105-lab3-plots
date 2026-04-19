"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

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

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot scatter plot of sensor temperatures vs time on given Axes.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings from Sensor A.
    sensor_b : array_like
        Temperature readings from Sensor B.
    timestamps : array_like
        Time stamps for the readings.
    ax : matplotlib.axes.Axes
        The Axes object to plot on.

    Returns
    -------
    None
        Modifies ax in place.
    """
    ax.scatter(timestamps, sensor_a, c="tab:blue", alpha=0.7, label="Sensor A")
    ax.scatter(timestamps, sensor_b, c="tab:orange", alpha=0.7, label="Sensor B")
    ax.set_title("Sensor Temperatures vs Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(alpha=0.3)

def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid histogram of sensor temperature distributions on given Axes.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings from Sensor A.
    sensor_b : array_like
        Temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object to plot on.

    Returns
    -------
    None
        Modifies ax in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='tab:blue', label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, color='tab:orange', label='Sensor B')
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)
    ax.axvline(mean_a, color='tab:blue', linestyle='--', linewidth=2, label='Mean A')
    ax.axvline(mean_b, color='tab:orange', linestyle='--', linewidth=2, label='Mean B')
    ax.set_title('Temperature Distribution for Sensor A and Sensor B')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.legend()
    ax.grid(alpha=0.3)