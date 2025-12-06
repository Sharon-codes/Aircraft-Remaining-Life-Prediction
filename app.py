
from flask import Flask, request
import sys
import json
import os
import pandas as pd
import numpy as np
from Turbofan.logger import logging
from Turbofan.exception import TurboException
from Turbofan.constant import get_current_time_stamp, CONFIG_DIR
from Turbofan.entity.Turbofan_predictor import TurbofanPredictor, TurbofanData
from flask import send_file, abort, render_template

## Defining constants:
ROOT_DIR = os.getcwd()
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)
TURBOFAN_DATA_KEY = "Turbofan_data"
RUL_VALUE_KEY = "RUL"

## Creating Flask Application:
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    context = {
        TURBOFAN_DATA_KEY: None,
        RUL_VALUE_KEY: None
    }

    if request.method == 'POST':
        engineNumber = int(request.form['engineNumber'])
        cycleNumber = int(request.form['cycleNumber'])
        sensor2 = float(request.form['sensor2'])
        sensor3 = float(request.form['sensor3'])
        sensor4 = float(request.form['sensor4'])
        sensor7 = float(request.form['sensor7'])
        sensor8 = float(request.form['sensor8'])
        sensor9 = float(request.form['sensor9'])
        sensor11 = float(request.form['sensor11'])
        sensor12 = float(request.form['sensor12'])
        sensor13 = float(request.form['sensor13'])
        sensor14 = float(request.form['sensor14'])
        sensor15 = float(request.form['sensor15'])
        sensor17 = float(request.form['sensor17'])
        sensor20 = float(request.form['sensor20'])
        sensor21 = float(request.form['sensor21'])

        Turbofan_data = TurbofanData(
            engineNumber=engineNumber,
            cycleNumber=cycleNumber,
            sensor2=sensor2,
            sensor3=sensor3,
            sensor4=sensor4,
            sensor7=sensor7,
            sensor8=sensor8,
            sensor9=sensor9,
            sensor11=sensor11,
            sensor12=sensor12,
            sensor13=sensor13,
            sensor14=sensor14,
            sensor15=sensor15,
            sensor17=sensor17,
            sensor20=sensor20,
            sensor21=sensor21)

        Turbofan_df = Turbofan_data.get_Turbofan_data_dataframe()
        Turbofan_predictor = TurbofanPredictor(model_dir=MODEL_DIR)

        RUL = Turbofan_predictor.predict(X=Turbofan_df)
        context = {
            TURBOFAN_DATA_KEY: Turbofan_data.get_Turbofan_data_as_dict(),
            RUL_VALUE_KEY: RUL,
        }
        return render_template('predict.html', context=context)
    return render_template("predict.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
