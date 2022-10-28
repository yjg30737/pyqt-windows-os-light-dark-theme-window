from enum import Enum


# see documentation here if you want to know about this C things
# https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute?source=recommendations
class DWMWINDOWATTRIBUTE(Enum):
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20