import requests
import grequests
import json
from requests import Timeout


def connection(places, place):
    """Connection with weather api"""
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={places[place][0]}' \
          f'&lon={places[place][1]}&appid=8537d9ef6386cb97156fd47d832f479c'
    return url


def one_connect(lats, lons):
    """Connection for one place"""
    params = {
        'lat': lats,
        'lon': lons,
        'appid': '8537d9ef6386cb97156fd47d832f479c'
    }

    url = 'https://api.openweathermap.org/data/2.5/weather'

    with requests.Session() as sess:
        try:
            r = sess.get(url, params=params, timeout=1)
        except Timeout:
            print('Timeout')
            return {'name': 'Timeout'}
        except Exception as ex:
            print(ex)
            return {}
        else:
            return r.json()


def get_responses_lst(places):
    """Async connections and mapping"""
    places_urls, async_list, lst = [], [], []

    for place in range(len(places)):
        places_urls.append(connection(places, place))

    for u in places_urls:
        action_item = grequests.get(u)
        async_list.append(action_item)

    for resp in grequests.map(async_list):
        lst.append(json.loads(resp.text))

    return lst
