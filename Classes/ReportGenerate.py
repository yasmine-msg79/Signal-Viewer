import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QMessageBox
from PyQt5.QtCore import QTimer
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

class SignalReportGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.initialize_real_time_data()
        def setup_ui(self):
        # Setting up the main layout and widgets
        self.layout = QVBoxLayout()
        
        # Label to guide the user
        self.layout.addWidget(QLabel("Choose a Signal for Your Report:"))

        # Dropdown menu for signal selection
        self.signal_dropdown = QComboBox(self)
        self.signal_dropdown.addItems(["ECG", "EMG", "EEG"])  # Available signal options
        self.layout.addWidget(self.signal_dropdown)

        # Button to generate the report
        self.generate_button = QPushButton("Create Report", self)
        self.generate_button.clicked.connect(self.generate_report)
        self.layout.addWidget(self.generate_button)

        # Setting the layout for the main window
        self.setLayout(self.layout)

    def initialize_real_time_data(self):
        # Initializing data storage for real-time signals
        self.signal_data = {
            "ECG": [],
            "EMG": [],
            "EEG": []
        }

        # Timer to simulate real-time data updates every 500 milliseconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_real_time_data)
        self.timer.start(500)  # Updates every half a second

    def update_real_time_data(self):
        # Simulating the generation of new data points
        for signal_type in self.signal_data.keys():
            new_value = random.uniform(-1, 1)  # Simulated real-time data value
            self.signal_data[signal_type].append(new_value)
            
            # Limit the length of the data array for memory management
            if len(self.signal_data[signal_type]) > 1000:  # Keep the latest 1000 data points
                self.signal_data[signal_type].pop(0)

    def generate_report(self):
        # When the user clicks to generate the report
        selected_signal_name = self.signal_dropdown.currentText()
        
        # Fetch the latest data for the chosen signal
        selected_signal_data = self.signal_data[selected_signal_name]
        
        # Calculate basic statistics for the report
        mean = sum(selected_signal_data) / len(selected_signal_data) if selected_signal_data else 0
        std_dev = (sum((x - mean) ** 2 for x in selected_signal_data) / len(selected_signal_data)) ** 0.5 if selected_signal_data else 0
        min_value = min(selected_signal_data, default=0)
        max_value = max(selected_signal_data, default=0)
        duration = len(selected_signal_data) * 0.5  # Assuming each data point represents 0.5 seconds
        
        # Prepare the statistics for the report
        stats = [{
            "Signal": selected_signal_name,
            "Mean": mean,
            "Std Dev": std_dev,
            "Min": min_value,
            "Max": max_value,
            "Duration": duration
        }]
        
        # Create a placeholder for snapshots (if needed)
        snapshots = ["snapshot1.png"]  # This can be replaced with actual image paths

        # Generate the PDF report
        self.create_pdf_report(stats, snapshots)

    def create_pdf_report(self, stats, snapshots, filename="signal_report.pdf"):
        """Creates a PDF report with the calculated statistics and any relevant snapshots."""
        pdf = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()

        # Adding a title to the report
        title = Paragraph("Your Real-Time Signal Report", styles['Title'])
        elements.append(title)
        elements.append(Spacer(1, 0.5 * inch))

        intro = Paragraph("Here are the statistics for the signal you selected:", styles['Normal'])
        elements.append(intro)
        elements.append(Spacer(1, 0.2 * inch))

        # Setting up the statistics table
        table_data = [["Signal Type", "Mean", "Std Dev", "Min", "Max", "Duration (s)"]]
        for stat in stats:
            table_data.append([
                stat.get("Signal", "Unknown"),
                f"{stat.get('Mean', 0):.2f}",
                f"{stat.get('Std Dev', 0):.2f}",
                f"{stat.get('Min', 0):.2f}",
                f"{stat.get('Max', 0):.2f}",
                f"{stat.get('Duration', 0):.2f}"
            ])

        # Creating the table and applying formatting
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 0.5 * inch))

        # Section for signal snapshots
        snapshot_title = Paragraph("Signal Snapshots", styles['Heading2'])
        elements.append(snapshot_title)
        elements.append(Spacer(1, 0.2 * inch))

        # Adding snapshots to the PDF
        for snapshot in snapshots:
            if os.path.exists(snapshot):
                elements.append(Paragraph(f"Snapshot for {os.path.basename(snapshot)}", styles['Normal']))
                elements.append(Spacer(1, 0.1 * inch))
                elements.append(Image(snapshot, width=5 * inch, height=3 * inch))
                elements.append(Spacer(1, 0.3 * inch))
            else:
                elements.append(Paragraph(f"Oops! Snapshot file not found: {snapshot}", styles['Normal']))
                elements.append(Spacer(1, 0.3 * inch))

        # Finalize the PDF document
        pdf.build(elements)
        
        
        QMessageBox.information(self, "Success!", "Your report has been successfully created and saved!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    report_widget = SignalReportGenerator()
    report_widget.setWindowTitle("Real-Time Signal Report Generator")
    report_widget.resize(400, 300)
    report_widget.show()
    sys.exit(app.exec_())

        
