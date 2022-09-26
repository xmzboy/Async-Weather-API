import unittest
import datetime
import rec_data
import connections


class TestClass(unittest.TestCase):
    def test_get_season(self):
        seasons = {(12, 1, 2): 'Winter', (3, 4, 5): 'Spring', (6, 7, 8): 'Summer', (9, 10, 11): 'Fall'}
        for k, v in seasons.items():
            if datetime.date.today().month in k:
                TestClass.assertEqual(self, rec_data.get_season({'coord': {'lat': 15}}), v)

    def test_connection(self):
        TestClass.assertEqual(self, connections.connection([(59.94, 30.314)], 0), 'https://api.openweathermap.org/data/2.5/weather?lat=59.94&lon=30.314&appid=8537d9ef6386cb97156fd47d832f479c')



if __name__ == '__main__':
    unittest.main()
