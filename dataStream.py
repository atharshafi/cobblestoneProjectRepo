# data_stream.py

import numpy as np
import time

def generate_data_stream(num_points=1000):
    """Simulates a data stream with regular patterns, seasonality, and noise."""
    base_pattern = np.sin(np.linspace(0, 10, num_points))  # Regular sine pattern
    noise = np.random.normal(0, 0.1, num_points)          # Random noise
    seasonal_component = np.sin(np.linspace(0, 5, num_points) * 2)  # Seasonal variations

    return base_pattern + noise + seasonal_component

def stream_data(num_points=1000, delay=0.05):
    """Generator function that yields data points with a delay."""
    data = generate_data_stream(num_points)
    for value in data:
        yield value
        time.sleep(delay)  # Simulate real-time streaming
