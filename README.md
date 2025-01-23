# Real-Time Signal Viewer

A sophisticated Python-based application designed for real-time visualization and analysis of signal data, offering comprehensive viewing and control capabilities.

## Project Overview

This application serves as a powerful tool for visualizing and analyzing multi-channel signals in real-time. It combines advanced signal processing capabilities with an intuitive user interface, making it suitable for various signal analysis applications, from EEG to EMG data visualization.

## Key Features

### Signal Visualization
- **Multi-channel Display**: Simultaneous visualization of multiple signal channels
- **Real-time Monitoring**: Live signal data processing and display
- **Dual Graph System**: Synchronized dual display with linking capabilities
- **Non-rectangular Plotting**: Advanced plotting options for specialized visualization

### Control Features
- **Playback Controls**
  - Play/Pause functionality
  - Rewind capability
  - Custom playback speeds

### Signal Management
- **Channel Controls**
  - Individual channel selection
  - Channel hiding/showing options
  - Channel gluing functionality
  - Custom color assignments

### View Customization
- **Display Options**
  - Adjustable view range
  - Dynamic zoom functionality
  - Flexible scaling options

### Documentation
- **Report Generation**
  - Snapshot capture system
  - Custom report creation
  - PDF export functionality

## Technical Stack

### Dependencies
- Python 3.x
- PyQt6 - UI Framework
- PyQtGraph - Scientific Plotting
- ReportLab - PDF Generation
- NumPy - Numerical Operations

### Project Structure
```tree
├── Classes/
│   ├── ChannelViewer.py     # Main visualization component
│   ├── NonRectangular.py    # Special plotting functionality
│   └── ReportGenerate.py    # Report generation system
├── Data/
│   ├── EEG.csv
│   ├── emg_healthy.csv
│   ├── emg_neuropathy.csv
│   ├── rec_1r.csv
│   └── rec_2f.csv
├── UI/
│   ├── channel_viewer.ui
│   ├── control_panel.ui
│   └── Non_rectangular.ui
└── MainWindowApp.py         # Application entry point


## Demo 
https://github.com/user-attachments/assets/20e02fe8-04ad-4676-99cf-69a11991a968




## Contributors

| Name | GitHub |
| ---- | ------ |

 Mostafa Mousa     [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/MostafaMousaaa) 

 Yasmine Gaballa     [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/yasmine-msg79)


 Ayatullah Ahmed     [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/Ayatullah-ahmed)



 Farha     [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/farha1010)
