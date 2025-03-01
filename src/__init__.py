from PyQt5.QtWidgets import QApplication
import sys
from src.MainWindow import SpursAPI

def run():
  app = QApplication(sys.argv)
  window = SpursAPI()
  window.show()
  sys.exit(app.exec_())