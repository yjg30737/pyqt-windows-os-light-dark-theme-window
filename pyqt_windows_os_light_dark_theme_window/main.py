from ctypes import byref, c_bool, sizeof, windll
from ctypes.wintypes import BOOL, MSG
from winreg import QueryValueEx, ConnectRegistry, HKEY_CURRENT_USER, OpenKey, KEY_READ

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from pyqt_windows_os_light_dark_theme_window.c import DWMWINDOWATTRIBUTE


class Window(QWidget):
    changedToDark = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        # init windows library and get function to handle the Windows theme
        dwmapi = windll.LoadLibrary("dwmapi")
        self.__dwmSetWindowAttribute = dwmapi.DwmSetWindowAttribute

        self.__detect_theme_flag = True

        self.__initTheme()

    # set current Windows theme first
    def __initTheme(self):
        self.__setCurrentWindowsTheme()

    # detect Windows theme change
    def nativeEvent(self, e, message):
        if self.isDetectingThemeAllowed():
            msg = MSG.from_address(message.__int__())
            # detect Windows theme changed (26 = WM_SETTINGCHANGE)
            # see more info https://learn.microsoft.com/en-us/windows/win32/winmsg/wm-settingchange
            if msg.message == 26:
                # if it changed, set new theme
                self.__setCurrentWindowsTheme()
        return super().nativeEvent(e, message)


    # set Windows theme by referring registry key
    def __setCurrentWindowsTheme(self):
        try:
            root = ConnectRegistry(None, HKEY_CURRENT_USER)
            root_key = OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', 0, KEY_READ)
            lightThemeValue, regtype = QueryValueEx(root_key, 'AppsUseLightTheme')
            if lightThemeValue == 0 or lightThemeValue == 1:
                self.__dwmSetWindowAttribute(int(self.winId()), DWMWINDOWATTRIBUTE.DWMWA_USE_IMMERSIVE_DARK_MODE.value, byref(c_bool(lightThemeValue == 0)), sizeof(BOOL))
                self.changedToDark.emit(lightThemeValue == 0)
            else:
                raise Exception(f'Unknown value "{lightThemeValue}".')
        except FileNotFoundError:
            print('AppsUseLightTheme not found.')
        except Exception as e:
            print(e)

    # set dark theme directly
    def setDarkTheme(self, f: bool):
        self.__dwmSetWindowAttribute(int(self.winId()), DWMWINDOWATTRIBUTE.DWMWA_USE_IMMERSIVE_DARK_MODE.value,
                                     byref(c_bool(f)), sizeof(BOOL))
        self.changedToDark.emit(f)
        if self.isMaximized() or self.isFullScreen() or self.maximumWidth() == self.width():
            if self.isMaximized():
                self.showNormal()
                self.showMaximized()
            elif self.isFullScreen():
                self.showNormal()
                self.showFullScreen()
            elif self.maximumWidth() == self.width():
                self.resize(self.width()-1, self.height())
                self.resize(self.width()+1, self.height())
        else:
            self.resize(self.width()+1, self.height())
            self.resize(self.width()-1, self.height())

    def isDetectingThemeAllowed(self):
        return self.__detect_theme_flag

    def allowDetectingTheme(self, f: bool):
        self.__detect_theme_flag = f

