# from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QVBoxLayout, QGraphicsOpacityEffect
# from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
# from PyQt5.QtGui import QFont
# import sys

# class FadeLabel(QLabel):
#     def __init__(self, text, parent=None, style="color: white"):
#         super().__init__(text, parent)
#         self.setAlignment(Qt.AlignCenter)
#         self.setFont(QFont("Sigmar", 50, QFont.Bold))
#         self.setStyleSheet(style)
#         self.opacity_effect = QGraphicsOpacityEffect(self)
#         self.setGraphicsEffect(self.opacity_effect)
        
#         self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
#         self.animation.setDuration(3000)
#         self.animation.setStartValue(0)
#         self.animation.setEndValue(1)
        
#     def fadeIn(self):
#         self.animation.start()

# class FadeButton(QPushButton):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self.setStyleSheet("font-size: 18px; padding: 10px;")
#         self.opacity_effect = QGraphicsOpacityEffect(self)
#         self.setGraphicsEffect(self.opacity_effect)
#         self.opacity_effect.setOpacity(0)
        
#         self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
#         self.animation.setDuration(2000)
#         self.animation.setStartValue(0)
#         self.animation.setEndValue(1)
        
#     def fadeIn(self):
#         self.animation.start()

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Fade-in Animation")
#         self.setGeometry(300, 200, 400, 300)
        
#         layout = QVBoxLayout()
#         self.label = FadeLabel("Welcome to PyQt5!", self)
#         self.button = FadeButton("Click Me", self)
        
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)
#         self.setLayout(layout)
        
#         # تشغيل تأثير الـ Fade-in عند بدء التطبيق
#         self.label.fadeIn()
        
#         # تشغيل تأثير الـ Fade-in للزر بعد انتهاء أنيميشن النص
#         self.label.animation.finished.connect(self.button.fadeIn)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())




from src import run

if __name__ == "__main__":
  run()