import emoji


SEASONS = {(12, 1, 2): 'Winter', (3, 4, 5): 'Spring', (6, 7, 8): 'Summer', (9, 10, 11): 'Fall'}

WEATHER_STATUS = {'Rain': emoji.emojize('rain :umbrella_with_rain_drops:'),
                  'Clear': emoji.emojize('sun :sun:'),
                  'Clouds': emoji.emojize('clouds :cloud:'),
                  'Snow': emoji.emojize('snow :snowflake:'),
                  'Fog': emoji.emojize('fog :fog:'),
                  'Mist': emoji.emojize('mist :fog:'),
                  'Drizzle': emoji.emojize('drizzle :umbrella:')}
