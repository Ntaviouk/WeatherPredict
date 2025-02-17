import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def generate_model(prcp, snow, wdir, wspd, wpgt, pres, tsun, tavg):
    data = {
        'prcp': prcp,
        'snow': snow,
        'wdir': wdir,
        'wspd': wspd,
        'wpgt': wpgt,
        'pres': pres,
        'tsun': tsun,
        'tavg': tavg
    }
    df = pd.DataFrame(data)

    X = df[['prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun']]
    y = df['tavg']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

    joblib.dump(model, 'temperature_model.pkl')


def predict_temperature(prcp, snow, wdir, wspd, wpgt, pres, tsun):
    model = joblib.load('temperature_model.pkl')
    input_data = pd.DataFrame([[prcp, snow, wdir, wspd, wpgt, pres, tsun]],
                              columns=['prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun'])
    prediction = model.predict(input_data)
    return prediction[0]


