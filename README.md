# Smart Speed Breaker Monitor

A Python-based application that monitors vehicle speeds using computer vision and provides real-time alerts for speed violations. This system is designed to help enforce speed limits and maintain road safety.

## Features

- 🚗 Real-time speed monitoring using webcam
- 📸 Automatic image capture of speeding vehicles
- 📊 Interactive data visualization
- 📝 Detailed logging of all vehicle passes
- 🔍 Filtering and export capabilities
- 📱 User-friendly GUI interface

## Requirements

- Python 3.x
- Webcam
- Required Python packages:
  - tkinter
  - opencv-python (cv2)
  - PIL (Pillow)
  - matplotlib
  - numpy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart-speed-breaker-monitor.git
cd smart-speed-breaker-monitor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python cccc.py
```

2. Click "Start Monitoring" to begin speed detection
3. The application will:
   - Monitor vehicle speeds in real-time
   - Capture images of speeding vehicles
   - Log all vehicle passes
   - Display results in the GUI

## Features in Detail

### Real-time Monitoring
- Monitors vehicle speeds using computer vision
- Configurable speed limit (default: 50 km/h)
- Real-time status updates

### Data Management
- Automatic logging of all vehicle passes
- Export capabilities for violation data
- Data visualization with graphs
- Filter to show only violations

### Image Capture
- Automatic capture of speeding vehicles
- Image storage in dedicated directory
- Double-click to view captured images

## Configuration

The following parameters can be modified in the code:
- `SENSOR_DISTANCE_METERS`: Distance between sensors (default: 0.55m)
- `SPEED_LIMIT_KMPH`: Speed limit threshold (default: 50 km/h)
- `IMAGE_DIR`: Directory for storing captured images
- `LOG_FILE`: CSV file for logging speed data

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenCV for computer vision capabilities
- Tkinter for GUI implementation
- Matplotlib for data visualization

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository. 