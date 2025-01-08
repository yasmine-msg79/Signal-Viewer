import sys
import os
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QMessageBox, \
    QListWidget, QAbstractItemView, QFileDialog
from PyQt6.QtCore import QTimer
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from Classes import ChannelViewer


class SignalReportGenerator(QWidget):
    def __init__(self, snapshots_list,*args, **kwargs):
        super(SignalReportGenerator, self).__init__(*args, **kwargs)
        self.timer = None
        self.signal_data = None
        self.generate_button = None
        self.snapshot_list = None
        self.layout = None
        self.snapshots = snapshots_list  # List of snapshots passed from ChannelViewer
        self.setup_ui()
        self.initialize_real_time_data()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        # Label to guide the user
        self.layout.addWidget(QLabel("Choose Snapshots for Your Report:"))

        # Dropdown menu for snapshot selection (changed to QListWidget for multiple selections)
        self.snapshot_list = QListWidget(self)
        self.snapshot_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        # Populate the list with snapshots
        for snapshot in self.snapshots:
            self.snapshot_list.addItem(snapshot['name'])  # Display snapshot names
        self.layout.addWidget(self.snapshot_list)

        # Button to generate the report
        self.generate_button = QPushButton("Create Report", self)
        self.generate_button.clicked.connect(self.generate_report)
        self.layout.addWidget(self.generate_button)

        # Setting the layout for the main window
        self.setLayout(self.layout)

    def initialize_real_time_data(self):
        # Initializing data storage for real-time signals (this part is kept for stats generation)
        self.signal_data = {
            "Signal": []
        }

        # Timer to simulate real-time data updates every 500 milliseconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_real_time_data)
        self.timer.start(500)  # Updates every half a second

    def update_real_time_data(self):
        # Simulating the generation of new data points
        new_value = random.uniform(-1, 1)  # Simulated real-time data value
        self.signal_data["Signal"].append(new_value)

        # Limit the length of the data array for memory management
        if len(self.signal_data["Signal"]) > 1000:
            self.signal_data["Signal"].pop(0)
   
    def generate_report(self):
        # Get selected snapshots from the list
        selected_items = self.snapshot_list.selectedItems()
        selected_snapshots = [item.text() for item in selected_items]

        if not selected_snapshots:
            QMessageBox.warning(self, "No Selection", "Please select at least one snapshot.")
            return

        # Fetch the latest data for the chosen signal (using 'Signal')
        selected_signal_data = self.signal_data["Signal"]

        stats = ChannelViewer.get_signal_stat()


        # Simplified file dialog without options
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Report As",
            "",
            "PDF Files (*.pdf);;All Files (*)"
        )
        
        if file_path:
            # Generate PDF report with the selected snapshots
            self.create_pdf_report(stats, selected_snapshots, filename=file_path)

    def create_pdf_report(self, stats, selected_snapshots, filename="signal_report_with_snapshots.pdf"):
        """Creates a PDF report with the selected snapshots."""
        pdf = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()

        # Adding a title to the report
        title = Paragraph("Your Snapshot Report", styles['Title'])
        elements.append(title)
        elements.append(Spacer(1, 0.5 * inch))

        intro = Paragraph("Here are the statistics for the selected snapshots:", styles['Normal'])
        elements.append(intro)
        elements.append(Spacer(1, 0.2 * inch))

        # Statistics table (using 'Signal')
        table_data = [["Mean", "Std", "Min", "Max", "Duration (s)"]]
        for stat in stats:
            table_data.append([
                f"{stat.get('Mean', 0):.2f}",
                f"{stat.get('Std', 0):.2f}",
                f"{stat.get('Min', 0):.2f}",
                f"{stat.get('Max', 0):.2f}",
                f"{stat.get('Duration', 0):.2f}"
            ])

        # Creating the table and formatting
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

        # Adding the snapshots to the PDF
        snapshot_title = Paragraph("Selected Snapshots", styles['Heading2'])
        elements.append(snapshot_title)
        elements.append(Spacer(1, 0.2 * inch))

        for snapshot_name in selected_snapshots:
            snapshot_path = f"{snapshot_name}"
            if os.path.exists(snapshot_path):
                elements.append(Paragraph(f"Snapshot: {snapshot_name}", styles['Normal']))
                elements.append(Spacer(1, 0.1 * inch))
                elements.append(Image(snapshot_path, width=5 * inch, height=3 * inch))
                elements.append(Spacer(1, 0.3 * inch))
            else:
                elements.append(Paragraph(f"Snapshot not found: {snapshot_name}", styles['Normal']))
                elements.append(Spacer(1, 0.3 * inch))

        # Finalize the PDF document
        pdf.build(elements)
        QMessageBox.information(self, "Success!", "Your report has been successfully created and saved!")
        def generate_report_alternative(self):
            # Get selected snapshots from the list
            selected_items = self.snapshot_list.selectedItems()
            selected_snapshots = [item.text() for item in selected_items]

            if not selected_snapshots:
                QMessageBox.warning(self, "No Selection", "Please select at least one snapshot.")
                return

            # Fetch the latest data for the chosen signal (using 'Signal')
            selected_signal_data = self.signal_data["Signal"]

            stats = ChannelViewer.get_signal_stat()
            # stats = [   # Example statistics data
            #     {'Mean': 0.5, 'Std': 0.1, 'Min': 0.3, 'Max': 0.7, 'Duration': 10},
            #     {'Mean': 0.6, 'Std': 0.2, 'Min': 0.4, 'Max': 0.8, 'Duration': 10},
            #     {'Mean': 0.7, 'Std': 0.3, 'Min': 0.5, 'Max': 0.9, 'Duration': 10}
            # ]

            # Simplified file dialog without options
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Report As",
                "",
                "Text Files (*.txt);;All Files (*)"
            )

            if file_path:
                # Generate text report with the selected snapshots
                self.create_text_report(stats, selected_snapshots, filename=file_path)

        def create_text_report(self, stats, selected_snapshots, filename="signal_report_with_snapshots.txt"):
            """Creates a text report with the selected snapshots."""
            with open(filename, 'w') as file:
                file.write("Your Snapshot Report\n")
                file.write("====================\n\n")
                file.write("Here are the statistics for the selected snapshots:\n\n")

                # Statistics table (using 'Signal')
                file.write("Mean\tStd\tMin\tMax\tDuration (s)\n")
                for stat in stats:
                    file.write(f"{stat.get('Mean', 0):.2f}\t{stat.get('Std', 0):.2f}\t{stat.get('Min', 0):.2f}\t{stat.get('Max', 0):.2f}\t{stat.get('Duration', 0):.2f}\n")

                file.write("\nSelected Snapshots:\n")
                for snapshot_name in selected_snapshots:
                    snapshot_path = f"{snapshot_name}"
                    if os.path.exists(snapshot_path):
                        file.write(f"Snapshot: {snapshot_name}\n")
                    else:
                        file.write(f"Snapshot not found: {snapshot_name}\n")

            QMessageBox.information(self, "Success!", "Your report has been successfully created and saved!")


if __name__ == '__main__':
    # Example snapshot data passed from ChannelViewer
    snapshots = [{'name': 'snapshot_1.png'}, {'name': 'snapshot_2.png'}, {'name': 'snapshot_3.png'}]

    app = QApplication(sys.argv)
    report_widget = SignalReportGenerator(snapshots)
    report_widget.setWindowTitle("Snapshot Report Generator")
    report_widget.resize(400, 300)
    report_widget.show()
    sys.exit(app.exec())
