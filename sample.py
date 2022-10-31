from PyQt5.QtWidgets import QPushButton, QGridLayout, QApplication

from pyqt_windows_os_light_dark_theme_window.main import Window


class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('Theme Toggle')
        btn.setCheckable(True)
        btn.toggled.connect(self.__themeToggled)
        lay = QGridLayout()
        lay.addWidget(btn)
        self.setLayout(lay)

    def __themeToggled(self, f):
        self.setDarkTheme(f)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())