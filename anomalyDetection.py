# anomaly_detection.py

import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=50, threshold=2.5):
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = []

    def detect(self, new_value):
        """Detect if the new value is an anomaly."""
        self.data_window.append(new_value)

        if len(self.data_window) > self.window_size:
            self.data_window.pop(0)  # Maintain a fixed window size

        if len(self.data_window) < self.window_size:
            return False  # Not enough data to detect anomalies yet

        # Calculate z-score for the new value
        mean = np.mean(self.data_window)
        std = np.std(self.data_window)
        z_score = (new_value - mean) / std if std != 0 else 0

        return abs(z_score) > self.threshold
