# main.py
from temperature_prediction import generate_model, predict_temperature
from scraper import get_weather_data as gd


def main():
    generate_model(gd("prcp"), gd("snow"), gd("wdir"), gd("wspd"), gd("wpgt"), gd("pres"),
                   gd("tsun"), gd("tavg"))

    print(predict_temperature(0.1, 110.0, 247.0, 6.7, 31.5, 1013.9, 0.0))


if __name__ == '__main__':
    main()
