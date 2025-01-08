# Real-Time Signal Viewer

A Python-based application for real-time visualization and analysis of signal data with multiple viewing and control capabilities.

## Features

- Multi-channel signal visualization
- Real-time signal monitoring 
- Dual graph display with linking capability
- Playback controls (Play, Pause, Rewind)
- Signal manipulation tools:
  - Channel selection
  - Color customization
  - View range control
  - Zoom functionality
  - Channel hiding/showing
- Non-rectangular plotting option
- Report generation with snapshots
- Channel gluing functionality

## Dependencies

- Python 3.x
- PyQt6
- PyQtGraph
- ReportLab
- NumPy

## Project Structure
├── Classes/ │ ├── ChannelViewer.py │ ├── NonRectangular.py │ └── ReportGenerate.py ├── Data/ │ ├── EEG.csv │ ├── emg_healthy.csv │ ├── emg_neuropathy.csv │ ├── rec_1r.csv │ └── rec_2f.csv ├── Icons/ ├── UI/ │ ├── channel_viewer.ui │ ├── control_panel.ui │ ├── Non_rectangular.ui │
