from TemperaturePrediction import generate_model, predict_temperature
from scraper4 import get_weather_data as gd


def main():
    generate_model(gd("prcp"), gd("snow"), gd("wdir"), gd("wspd"), gd("wpgt"), gd("pres"),
                   gd("tsun"), gd("tavg"))

    print(predict_temperature(0, 0, 0, 0, 0, 0, 0, ))


if __name__ == '__main__':
    main()
