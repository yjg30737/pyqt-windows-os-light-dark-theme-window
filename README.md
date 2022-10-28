# pyqt-windows-os-light-dark-theme-window
PyQt windows which detects Windows dark/light theme settings and changes the theme dynamically

## Requirements
* PyQt5

## Method Overview
* `setDarkTheme(f: bool)` - If you want to set Windows theme directly, use this. If you give `True`, dark theme will be set to qt window.
* `isDetectingThemeAllowed() -> bool` - Check if detecting theme feature is allowed.
* `allowDetectingTheme(f: bool)` - Allow detecting theme to change the Windows system theme in real-time. True in default.

## Preview
Windows light theme (as you expected)
![image](https://user-images.githubusercontent.com/55078043/198483498-00e238c9-0f1b-4782-81a4-6edf2a9be667.png)

Windows dark theme
![image](https://user-images.githubusercontent.com/55078043/198484079-b1bef3df-a126-4136-a073-cc17c322eced.png)
