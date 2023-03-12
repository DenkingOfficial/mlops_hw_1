#!/bin/bash
ACTIVATE_SCRIPT=".venv/Scripts/activate"
if [ ! -f $ACTIVATE_SCRIPT ]; then
    echo No virtual environment found
    
    echo Installing virtualenv
    python -m pip install --user virtualenv -q

    echo Creating venv
    python -m venv .venv

    echo Activating venv
    source $ACTIVATE_SCRIPT

    echo Installing requirements
    pip install -r requirements.txt -q
else
    echo Activating venv
    source $ACTIVATE_SCRIPT
fi

echo Model training process started

python data_creation.py

python model_preprocessing.py

python model_preparation.py

python model_testing.py
