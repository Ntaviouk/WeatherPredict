import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV


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

    param_grid = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 7]
    }

    model = xgb.XGBRegressor(random_state=42)
    grid_search = GridSearchCV(model, param_grid, cv=3, scoring='neg_mean_absolute_error', verbose=1, n_jobs=-1)
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_
    print("Best parameters:", grid_search.best_params_)

    y_pred = best_model.predict(X_test)
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

    best_model.save_model('temperature_xgb_model.json')


def predict_temperature(prcp, snow, wdir, wspd, wpgt, pres, tsun):
    model = xgb.XGBRegressor()
    model.load_model('temperature_xgb_model.json')

    input_data = pd.DataFrame([[prcp, snow, wdir, wspd, wpgt, pres, tsun]],
                              columns=['prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun'])
    prediction = model.predict(input_data)
    return prediction[0]
