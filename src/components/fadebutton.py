from PyQt5.QtWidgets import QPushButton, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation

class FadeButton(QPushButton):
  def __init__(self, text: str, parent=None ):
    super().__init__(text, parent)
    # self.setStyleSheet()
    self.opacity_effect = QGraphicsOpacityEffect(self)
    self.setGraphicsEffect(self.opacity_effect)
    self.opacity_effect.setOpacity(0)
    
    self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
    self.animation.setDuration(2000)
    self.animation.setStartValue(0)
    self.animation.setEndValue(1)
      
  def fadeIn(self):
    self.animation.start()