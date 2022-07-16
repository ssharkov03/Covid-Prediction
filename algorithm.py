import numpy as np
import pandas as pd

import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as MAE
from xgboost import XGBRegressor
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import cross_val_score
from numpy import absolute

# model and csv table must be at the same folder with this algo

def get_X_test(csv_table_name):
    
    df = pd.read_csv(csv_table_name, index_col=0)
    df.drop(["inf_rate", "has_metro"], axis=1, inplace=True)
    df = df.select_dtypes(include=np.number)
    
    return df


def get_inf_rate_prediction(csv_input_table_name, csv_answer_table_name, model_name, BOOL_save_to_csv):
    model = joblib.load(model_name)
    X_test = get_X_test(csv_input_table_name)
    y_pred = model.predict(X_test)
    
    if BOOL_save_to_csv:
        answer_df = pd.read_csv(csv_answer_table_name)
        answer_df['inf_rate'] = y_pred
        answer_df.to_csv("NSU-ES-Team.csv", index=None)
    return y_pred


def get_score(y_pred, y_test):
    return MAE(y_pred, y_test)


if __name__ == "__main__":
    get_inf_rate_prediction('validationData/covid_data_test.csv', 'validationData/NSU-ES-Team.csv', 'XGBmodel.joblib', True)