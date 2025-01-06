import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QGridLayout, QTableWidget, QTableWidgetItem, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class FunctionalTestGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Functional Test GUI")
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet(self.dark_theme())
        self.initUI()

    def initUI(self):
        # Main Container
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Header Buttons
        header_buttons = ["ARINC View", "Signal Plotter", "Functional Test", "Acceptance Tests", "Power Supplies"]
        header_layout = QHBoxLayout()

        for button_text in header_buttons:
            button = QPushButton(button_text)
            button.setFont(QFont("Arial", 10, QFont.Bold))
            button.setFixedHeight(40)
            button.setStyleSheet("QPushButton { color: white; background-color: #333; border: 1px solid #555; }"
                                 "QPushButton:hover { background-color: #555; }")
            header_layout.addWidget(button)

        # Status and Controls Section
        status_control_layout = QGridLayout()
        statuses = ["Fully Opened Status", "Closed Status", "Latched Status", "Unlatched Status",
                    "Locked Status", "Unlocked Status"]
        commands = ["Open Command", "Close Command", "Latch Command", "Unlatch Command",
                    "Lock Command", "Unlock Command"]

        for i, (status_text, command_text) in enumerate(zip(statuses, commands)):
            # Status Text
            status_label = QLabel(status_text)
            status_label.setFont(QFont("Arial", 12))
            status_label.setFixedHeight(40)
            status_label.setStyleSheet("QLabel { color: white; background-color: #2D2D2D; padding-left: 10px; }")

            # Status Indicator (Circle)
            indicator_container = QFrame()
            indicator_container.setFixedSize(40, 40)
            indicator_container.setStyleSheet("""
                QFrame {
                    border: none;
                    background-color: none;
                    border-radius: 20px;
                }
            """)
            indicator_layout = QHBoxLayout()
            indicator_circle = QLabel("●")
            indicator_circle.setAlignment(Qt.AlignCenter)
            indicator_circle.setStyleSheet("color: cyan; font-size: 25pt;")
            indicator_layout.addWidget(indicator_circle)
            indicator_container.setLayout(indicator_layout)

            # Command Label
            command_label = QLabel(command_text)
            command_label.setFont(QFont("Arial", 12))
            command_label.setFixedHeight(40)
            command_label.setStyleSheet("QLabel { color: white; background-color: #2D2D2D; padding-left: 10px; }")

            # Push Button for Command
            command_button = QPushButton("▶")
            command_button.setFixedSize(60, 40)
            command_button.setStyleSheet("""
                QPushButton {
                    color: white;
                    font-size: 18pt;
                    background-color: #2D2D2D;
                    border: 2px solid #555;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #444;
                }
            """)

            # Layout Row
            status_control_layout.addWidget(status_label, i, 0)  # Status Text
            status_control_layout.addWidget(indicator_container, i, 1)  # Status Indicator
            status_control_layout.addWidget(command_label, i, 2)  # Command Text
            status_control_layout.addWidget(command_button, i, 3)  # Command Button

        # Test History Table
        table = QTableWidget(5, 4)
        table.setHorizontalHeaderLabels(["Start Time", "Elapsed Time", "Status", "Test Name"])
        table.setFixedHeight(200)
        table.setStyleSheet("""
            QTableWidget {
                background-color: #222;
                color: white;
                gridline-color: #444;
            }
            QHeaderView::section {
                background-color: #333;
                color: white;
                font-weight: bold;
            }
        """)

        # Test Table Data
        data = [
            ["12 Dec - 14:21", "0.50 hr", "In Progress", "MCU1 Burn-in"],
            ["12 Dec - 13:26", "0.25 hr", "Complete", "Functional Test"],
            ["10 Dec - 12:14", "0.87 hr", "Interrupted", "Functional Test"],
            ["04 Dec - 10:36", "0.10 hr", "Complete", "MCU1 PBIT Verify"],
            ["04 Dec - 09:20", "0.26 hr", "Complete", "MCU1 I/O Range"]
        ]
        for row, (start, elapsed, status, test) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(start))
            table.setItem(row, 1, QTableWidgetItem(elapsed))
            table.setItem(row, 2, QTableWidgetItem(status))
            table.setItem(row, 3, QTableWidgetItem(test))

        # System Overview Placeholder
        system_overview = QLabel("System Overview Placeholder")
        system_overview.setAlignment(Qt.AlignCenter)
        system_overview.setFixedHeight(100)
        system_overview.setStyleSheet("color: lightgray; font-size: 14pt;")

        # Main Layout Organization
        main_layout.addLayout(header_layout)  # Header
        main_layout.addLayout(status_control_layout)  # Status and Controls
        main_layout.addWidget(table)  # Test History Table
        main_layout.addWidget(system_overview)  # System Overview Placeholder

        # Set Main Layout
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def dark_theme(self):
        """Dark Theme Stylesheet."""
        return """
            QWidget {
                background-color: #1E1E1E;
                color: white;
                font-family: Arial;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: #2D2D2D;
                border: 1px solid #555;
                color: white;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #3D3D3D;
            }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionalTestGUI()
    window.show()
    sys.exit(app.exec_())
