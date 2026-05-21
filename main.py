import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    """The primary window for the H_project diagnostic interface."""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.setWindowTitle("H_project - Diagnostic Interface")
        self.resize(800, 600)
        
        # Temporary placeholder label to test execution
        label = QLabel("H_project: Automated Diagnostic Interface", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

def main():
    """Application entry point."""
    print("Initialising H_project application...")
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())