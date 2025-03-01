from PyQt5.QtWidgets import QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QFont

class FadeLabel(QLabel):
  def __init__(self, text, parent=None, style="color: white"):
    super().__init__(text, parent)
    self.setAlignment(Qt.AlignCenter)
    self.setFont(QFont("Sigmar", 50, QFont.Bold))

    self.setStyleSheet(style)
    self.opacity_effect = QGraphicsOpacityEffect(self)
    self.setGraphicsEffect(self.opacity_effect)
    
    self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
    self.animation.setDuration(3000)
    self.animation.setStartValue(0)
    self.animation.setEndValue(1)
      
  def fadeIn(self):
    self.animation.start()