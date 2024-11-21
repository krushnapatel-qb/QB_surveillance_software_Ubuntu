from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMessageBox
from router import Router
import sys
from PyQt6.QtGui import QPalette, QIcon
from views import DashboardPage


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QB")
    main_window = Router()
    main_window.show()
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
