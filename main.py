# main.py

from anomalyDetection import AnomalyDetector
from dataStream import stream_data
from visualization import RealTimePlotter

def main():
    detector = AnomalyDetector(window_size=50, threshold=2.5)
    plotter = RealTimePlotter(window_size=100)

    # Stream the data and detect anomalies in real-time
    for value in stream_data(num_points=1000, delay=0.05):
        is_anomaly = detector.detect(value)
        plotter.update_plot(new_value=value, is_anomaly=is_anomaly)

if __name__ == "__main__":
    main()
