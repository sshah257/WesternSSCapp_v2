@echo off
cd %cd%

python get-pip.py
python -m pip install Pillow
python -m pip install paramiko