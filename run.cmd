@echo off
pyuic5 -x .\ui\interface.ui -o .\src\ui\Ui_interface.py
python -B SpursAPI.py