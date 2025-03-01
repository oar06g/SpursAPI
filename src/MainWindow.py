from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from PyQt5.QtCore import Qt

from src.ui.Ui_interface import Ui_SpursAPI
from src.components.fadelabel import FadeLabel
from src.components.fadebutton import FadeButton
from src.utils.loader import load_styles
from src.utils.checker import check_first_session
from src.utils.variables import PATH_DARK_MOD_STYLE


class SpursAPI(QMainWindow):
  def __init__(self):
    super(SpursAPI, self).__init__()
    self.ui = Ui_SpursAPI()
    self.ui.setupUi(self)
    check = check_first_session()
    if check == False: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)
    else: self.ui.stackedWidget.setCurrentWidget(self.ui.welcome_page)
    
    loadstyle_darkmod = load_styles(PATH_DARK_MOD_STYLE)
    self.setStyleSheet(loadstyle_darkmod)

    _layout_welcome = QVBoxLayout()
    _layout_welcome.setAlignment(Qt.AlignCenter)
    
    self.title_intro = FadeLabel("SpursAPI")
    self.title_intro.setObjectName("title_intro")

    self.login_btn = FadeButton("Login")
    self.login_btn.setObjectName("login_btn")
    
    _layout_welcome.addWidget(self.title_intro, alignment=Qt.AlignCenter)
    _layout_welcome.addWidget(self.login_btn, alignment=Qt.AlignCenter)
    
    self.ui.welcome_page.setLayout(_layout_welcome)

    self.title_intro.fadeIn()
    self.title_intro.animation.finished.connect(self.login_btn.fadeIn)
