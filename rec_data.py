import csv
import datetime
from constants import SEASONS


def get_season(dct):
    """Getting season for both hemispheres"""
    for k, v in SEASONS.items():
        if datetime.date.today().month in k:
            if dct['coord']['lat'] < 0:
                temp = datetime.date.today().month + 6
                if temp > 12:
                    temp -= 12
                for key in SEASONS.keys():
                    if temp in key:
                        return SEASONS[key]
            else:
                return v


def record_data(dct):
    """Recording data into csv file"""
    filename = f"data/{dct['name'].lower().replace(' ', '_')}_data.csv"
    season = get_season(dct)
    lst = [datetime.date.today().strftime('%d %B %Y'), season,
           dct['weather'][0]['main'], round(dct['main']['temp'] - 273),
           round(dct['main']['humidity']), round(dct['wind']['speed'])]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            final_data = f.readlines()[-1]
    except Exception as ex:
        print(ex)
        with open(filename, 'w', encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter=";", lineterminator="\r")
            file_writer.writerow(["Date", "Season", "Weather", "Temperature", "Humidity", "Wind Speed"])
            file_writer.writerow(lst)
    else:
        if final_data.split(';')[0] != lst[0]:
            with open(filename, 'a', encoding='utf-8') as f:
                file_writer = csv.writer(f, delimiter=";", lineterminator="\r")
                file_writer.writerow(lst)
