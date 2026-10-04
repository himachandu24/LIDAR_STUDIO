from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LIDAR Studio")
        self.resize(1200, 700)

        self._create_ui()

    def _create_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        navigation = self._create_navigation()
        self.pages = QStackedWidget()

        main_layout.addWidget(navigation)
        main_layout.addWidget(self.pages, 1)

    def _create_navigation(self):
        navigation = QWidget()
        navigation_layout = QVBoxLayout(navigation)

        title = QLabel("LIDAR Studio")
        navigation_layout.addWidget(title)

        dashboard_button = QPushButton("Dashboard")
        live_scan_button = QPushButton("Live Scan")
        recordings_button = QPushButton("Recordings")
        ros2_button = QPushButton("ROS 2")
        diagnostics_button = QPushButton("Diagnostics")
        settings_button = QPushButton("Settings")

        navigation_layout.addWidget(dashboard_button)
        navigation_layout.addWidget(live_scan_button)
        navigation_layout.addWidget(recordings_button)
        navigation_layout.addWidget(ros2_button)
        navigation_layout.addWidget(diagnostics_button)
        navigation_layout.addWidget(settings_button)

        navigation_layout.addStretch()

        return navigation