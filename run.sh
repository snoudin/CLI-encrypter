#!/bin/bash

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install PyQt5
python3 main.py
