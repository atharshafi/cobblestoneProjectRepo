# Efficient Data Stream Anomaly Detection

## Project Overview
This project implements an efficient Python script for real-time anomaly detection in a continuous data stream. The data stream simulates various metrics (such as financial transactions or system metrics), and the goal is to identify unusual patterns, such as exceptionally high values or deviations from the norm.

The project focuses on:
- Algorithm selection for real-time anomaly detection.
- Simulating a continuous data stream with noise, regular patterns, and occasional anomalies.
- Detecting anomalies in real-time.
- Optimizing performance for speed and efficiency.
- Providing a simple visualization tool for real-time data and anomaly visualization.

## Features
- **Algorithm Selection**: The project uses a Z-Score based method to detect anomalies, with customizable window size and threshold to handle different types of data streams.
- **Data Stream Simulation**: Simulates real-time data using a sine wave, noise, and occasional spikes to represent anomalies.
- **Anomaly Detection**: Implements a rolling window mechanism to detect anomalies based on statistical deviations.
- **Optimization**: Designed for efficiency using `deque` for a sliding window to maintain performance with continuous data.
- **Visualization**: Real-time plotting of the data stream and anomaly detection using Matplotlib.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How the Project Works](#How-the-Project-Works)
- [Algorithm Details](#algorithm-details)
- [Customization](#customization)
- [Project Structure](#project-structure)


## Installation
Clone the repository:
```bash
git clone https://github.com/your-username/data-stream-anomaly-detection.git
cd data-stream-anomaly-detection
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following libraries:
```
numpy
matplotlib
```

## Usage
To run the project, simply execute the Python script:
```bash
python anomaly_detection.py
```
### Data Stream
The script simulates a data stream with regular patterns (a sine wave), random noise, and occasional anomalies. The anomaly detector processes this stream in real time, identifying and flagging anomalies based on statistical deviations.

### Anomaly Detection
Anomalies are detected using the Z-Score method, which flags data points that are a certain number of standard deviations away from the rolling mean. You can adjust the sensitivity by modifying the `window_size` and `threshold` parameters in the `AnomalyDetector` class.

### Real-time Visualization
The script generates a live plot of the data stream, with detected anomalies highlighted in red. This allows you to visualize both the stream and the identified anomalies in real time.


# How-the-Project-Works

## Data Stream Simulation
The `stream_data` function in `data_stream.py` generates a continuous flow of data points that include regular patterns, noise, and seasonal variations.

## Anomaly Detection
The `AnomalyDetector` class in `anomaly_detection.py` uses a rolling window to calculate the mean and standard deviation of the recent data. It flags any value that deviates significantly from the normal distribution (based on a z-score).

## Real-time Visualization
The `RealTimePlotter` in `visualization.py` continuously updates the plot as the data streams in and highlights detected anomalies in red.

## Testing the Project
To test the project, simply run `main.py`, and a real-time plot of the data stream and anomalies will be displayed.

This structure provides a complete, efficient anomaly detection project with real-time capabilities. Let me know if you'd like to make further adjustments!

## Algorithm Details
The anomaly detection is based on the Z-Score method. Here’s how it works:
- The Z-Score measures how many standard deviations a data point is from the mean.
- A data point is flagged as an anomaly if its Z-Score exceeds a predefined threshold (default is 3 standard deviations).
- A rolling window is used to calculate the mean and standard deviation over a defined number of recent data points.

### Example of the Z-Score formula:
\[
Z=x−μ/σ
\]
Where:
- \( x \) is the new data point,
- \( \mu \) is the rolling mean,
- \( \sigma \) is the rolling standard deviation.

### Algorithm Parameters:
- **window_size**: The number of recent data points used to calculate the rolling mean and standard deviation.
- **threshold**: The number of standard deviations a new value must deviate from the mean to be considered an anomaly.

## Customization
- **Window Size**: Modify the `window_size` parameter to control how many recent points are used to compute the rolling statistics.
- **Threshold**: Adjust the threshold to control the sensitivity of anomaly detection. A lower threshold will detect more anomalies, while a higher threshold will be more conservative.

To change these parameters, modify the `AnomalyDetector` class instantiation:
```python
detector = AnomalyDetector(window_size=100, threshold=2.5)
```

## Project Structure
```
.
├── anomaly_detection.py   # Main Python script
├── README.md              # Project documentation (this file)
├── requirements.txt       # Dependencies
└── LICENSE                # License file (optional)
```

- **anomaly_detection.py**: The main script containing the data stream simulation, anomaly detection, and real-time visualization.
- **requirements.txt**: Lists all the external libraries required to run the project.
