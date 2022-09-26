import unittest
import rec_data
import datetime


class TestClass(unittest.TestCase):
    def test_get_season(self):
        seasons = {(12, 1, 2): 'Winter', (3, 4, 5): 'Spring', (6, 7, 8): 'Summer', (9, 10, 11): 'Fall'}
        for k, v in seasons.items():
            if datetime.date.today().month in k:
                TestClass.assertEqual(self, rec_data.get_season({'coord': {'lat': 15}}), v)


if __name__ == '__main__':
    unittest.main()
