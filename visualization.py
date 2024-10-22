# visualization.py

import matplotlib.pyplot as plt

class RealTimePlotter:
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.data = []
        self.anomalies = []

    def update_plot(self, new_value, is_anomaly=False):
        self.data.append(new_value)

        if len(self.data) > self.window_size:
            self.data.pop(0)

        if is_anomaly:
            self.anomalies.append(len(self.data) - 1)

        plt.clf()
        plt.plot(self.data, label="Data Stream")
        plt.scatter(self.anomalies, [self.data[i] for i in self.anomalies], color='red', label="Anomalies", zorder=5)
        plt.legend()
        plt.pause(0.01)
