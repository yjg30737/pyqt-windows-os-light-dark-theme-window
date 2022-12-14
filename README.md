# pyqt-windows-os-light-dark-theme-window
PyQt windows which detects Windows dark/light theme settings and changes the theme dynamically

<b>This is for Windows only.</b> I tested this in Windows 11. This app might work in Windows 10 as well.

## Detailed Description
This is using Windows `DWMAPI` library, `winreg` for get the window registry's value, `nativeEvent` to change the theme.

As you might know, Windows can change the theme light to dark, or dark to light. This window detects such a thing and apply it to the frame.

You can make it unable to detect the theme if you don't want to change the current window theme accordance with the system theme. See the Method Overview below.

## Requirements
* PyQt5

## Install
`git clone ~`

or

`python -m pip install pyqt-windows-os-light-dark-theme-window --upgrade` 

## Method/Signal Overview
### Methods
* `setDarkTheme(f: bool)` - If you want to set Windows theme directly, use this. If you give `True`, dark theme will be set to qt window.
* `isDetectingThemeAllowed() -> bool` - Check if detecting theme feature is allowed.
* `allowDetectingTheme(f: bool)` - Allow detecting theme to change the Windows system theme in real-time. True in default.
### Signal
* `changedToDark(bool)` - If theme changed, this signal will be emitted.

## Code Sample
Note: You don't need this code sample if you <b>cloned</b> this repo, just run the sample.py and you can see the fine result. This code sample is for the people who installed this with <b>pip</b>.
```python
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
        self.changedToDark.connect(self.__darkThemeOn)

    def __themeToggled(self, f):
        self.setDarkTheme(f)

    def __darkThemeOn(self, f):
        print(f'Is current theme dark?: {f}')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

## Preview
Windows light theme (as you expected)

![image](https://user-images.githubusercontent.com/55078043/198911732-adf7c8ee-4e9a-4b39-afd4-eef4acd862be.png)

Windows dark theme

![image](https://user-images.githubusercontent.com/55078043/198911760-71d7b16b-81d9-4df2-ad06-84c8693091f5.png)
