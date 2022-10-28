from setuptools import setup, find_packages

setup(
    name='pyqt-windows-os-light-dark-theme-window',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt windows which detects Windows dark/light theme settings and changes the theme dynamically',
    url='https://github.com/yjg30737/pyside-database-chart-example.git',
    install_requires=[
        'PyQt5'
    ]
)