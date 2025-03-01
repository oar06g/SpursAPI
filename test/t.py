from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QColor, QPalette, QBrush, QFont
import sys

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dark Mode Login")
        self.setGeometry(200, 200, 400, 500)

        # 🟢 تفعيل الـ Dark Mode
        self.setStyleSheet("background-color: #121212; color: white;")

        # 🌀 إنشاء الخلفية المتحركة
        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(50, 50, 300, 400)
        self.bg_label.setStyleSheet("background-color: rgba(50, 50, 50, 100); border-radius: 20px;")
        
        # ✨ تحريك الخلفية
        self.animation = QPropertyAnimation(self.bg_label, b"geometry")
        self.animation.setDuration(4000)
        self.animation.setStartValue(QRect(50, 50, 300, 400))
        self.animation.setEndValue(QRect(60, 60, 280, 380))
        self.animation.setLoopCount(-1)
        self.animation.start()

        # 📌 عناصر تسجيل الدخول
        self.title = QLabel("Login", self)
        self.title.setFont(QFont("Arial", 24, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet("background: #333; border: none; padding: 10px; border-radius: 5px; color: white;")

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("background: #333; border: none; padding: 10px; border-radius: 5px; color: white;")

        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("background: #6200ea; color: white; padding: 10px; border-radius: 5px; font-weight: bold;")

        # 🖇️ ترتيب العناصر
        layout = QVBoxLayout()
        layout.setContentsMargins(60, 100, 60, 100)  # هامش داخلي لجعل العناصر داخل الخلفية
        layout.addWidget(self.title)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)

        self.bg_label.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
