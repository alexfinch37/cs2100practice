"""
Testing the API
"""

import unittest

from nasaapi import is_valid_date
from nasaapi import process_nasa_response

##############################

class TestAPI(unittest.TestCase):
    """
    Let's test!!
    """

    def test_isvaliddate(self) -> None:
        """Tests is_valid_date"""

        # good and historical
        self.assertTrue(is_valid_date('2026-02-09'))
        self.assertTrue(is_valid_date('1776-07-04'))
        self.assertTrue(is_valid_date('1898-10-03'))

        # bad formats
        self.assertFalse(is_valid_date('Feb 06, 2026'))
        self.assertFalse(is_valid_date('02-06-2026'))

        # legal numbers, bad dates
        self.assertFalse(is_valid_date('2026-15-01'))
        self.assertFalse(is_valid_date('2026-02-99'))

        # leap years
        self.assertTrue(is_valid_date('2026-02-28'))
        self.assertFalse(is_valid_date('2026-02-29'))
        self.assertTrue(is_valid_date('2024-02-28'))
        self.assertTrue(is_valid_date('2024-02-29'))


    def test_processnasaresponse_good(self) -> None:
        """testing process_nasa_response with good inputs"""

        response1: dict[str, str] = {
            'date':'2026-02-06', 
            'title':'Supernova Remnant Cassiopeia A', 
            'explanation':'Massive stars in our Milky Way Galaxy live spectacular lives...', 
            'hdurl':'https://apod.nasa.gov/apod/image/2602/CasA_nircam_4096.jpg',
            'url':'https://apod.nasa.gov/apod/image/2602/CasA_nircam_1024.jpg'
        }

        response2: dict[str, str] = {
            'date':'2025-12-25', 
            'title':'Unicorn, Fox Fur and Christmas Tree', 
            'explanation':'A star forming region cataloged as NGC 2264...', 
            'url':'https://apod.nasa.gov/apod/image/2512/IMG_7311_800.jpeg',
            'hdurl':'https://apod.nasa.gov/apod/image/2512/IMG_7311.jpeg'
        }

        result_hd = process_nasa_response(True, response1)
        result_regular = process_nasa_response(False, response2)

        self.assertEqual(result_hd.date, response1['date'])
        self.assertEqual(result_hd.title, response1['title'])
        self.assertEqual(result_hd.explanation, response1['explanation'])
        self.assertEqual(result_hd.url, response1['hdurl'])

        self.assertEqual(result_regular.date, response2['date'])
        self.assertEqual(result_regular.title, response2['title'])
        self.assertEqual(result_regular.explanation, response2['explanation'])
        self.assertEqual(result_regular.url, response2['url'])


    def test_processnasaresponse_bad(self) -> None:
        """testing process_nasa_response with bad inputs"""

        for hd in (True, False):
            # none
            with self.assertRaises(KeyError):
                process_nasa_response(hd, {})

            # missing one
            with self.assertRaises(KeyError):
                process_nasa_response(hd, {
                    'title':'', 
                    'explanation':'', 
                    'hdurl':'', 
                    'url':''
                })

            with self.assertRaises(KeyError):
                process_nasa_response(hd, {
                    'date':'', 
                    'explanation':'', 
                    'hdurl':'', 
                    'url':''
                })

            with self.assertRaises(KeyError):
                process_nasa_response(hd, {
                    'date':'', 
                    'title':'', 
                    'hdurl':'', 
                    'url':''
                })

            with self.assertRaises(KeyError):
                process_nasa_response(hd, {
                    'date':'', 
                    'title':'', 
                    'explanation':'', 
                    'url':''
                })

            with self.assertRaises(KeyError):
                process_nasa_response(hd, {
                    'date':'',
                    'title':'',
                    'explanation':'',
                    'hdurl':'',
                })

if __name__ == "__main__":
    unittest.main()
