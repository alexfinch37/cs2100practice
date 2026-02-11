"""
Testing the API
"""

from typing import Callable

import unittest

from nasaapi import is_valid_date as is_valid_date_good
from nasaapi import process_nasa_response as process_nasa_response_good
from nasaapi import NasaPic

from badapi import (
    is_valid_date1,
    is_valid_date2,
    is_valid_date3,

    process_nasa_response1,
    process_nasa_response2,
    process_nasa_response3,
    process_nasa_response4,
    process_nasa_response5,
    process_nasa_response6,
)

##############################

class TestAPI(unittest.TestCase):
    """
    Let's test!!
    """

    def _test_isvaliddate(self, is_valid_date: Callable[[str], bool]) -> None:
        """TODO: put your tests here!!"""

        self.assertFalse(is_valid_date(''))
        self.assertTrue(is_valid_date('2026-02-09'))
        self.assertTrue(is_valid_date("2012-12-12"))
        self.assertFalse(is_valid_date("2029-13-32"))


    def test_isvaliddate(self) -> None:
        """Don't change"""

        bad_f = [
            is_valid_date1,
            is_valid_date2,
            is_valid_date3,
        ]

        good_passed = False

        print()
        try:
            self._test_isvaliddate(is_valid_date_good)
            print('is_validate: Passed the good function!')
            good_passed = True
        except: # pylint: disable=bare-except
            print('is_validate: Failed the good function :(')

        if good_passed:

            caught: int = 0

            for f in bad_f:
                try:
                    self._test_isvaliddate(f)
                except: # pylint: disable=bare-except
                    caught += 1

            print(f'is_validate: caught {caught}/{len(bad_f)}')

    ##################################################

    def _test_processnasaresponse(
        self,
        process_nasa_response: Callable[[bool, dict[str, str]], NasaPic]
    ) -> None:
        """TODO: put your tests here!!"""

        response: dict[str, str] = {
            'date':'2026-02-06', 
            'title':'Supernova Remnant Cassiopeia A', 
            'explanation':'Massive stars in our Milky Way Galaxy live spectacular lives...', 
            'hdurl':'https://apod.nasa.gov/apod/image/2602/CasA_nircam_4096.jpg',
            'url':'https://apod.nasa.gov/apod/image/2602/CasA_nircam_1024.jpg'
        }

        result = process_nasa_response(True, response)

        self.assertEqual(result.date, '2026-02-06')
        self.assertEqual(result.title, 'Supernova Remnant Cassiopeia A')
        self.assertNotEqual(result.title, 'Supernova Remnant Cassiopeia B')
        self.assertEqual(result.explanation, 'Massive stars in our Milky Way Galaxy live spectacular lives...')


    def test_processnasaresponse(self) -> None:
        """Don't change"""

        bad_f = [
            process_nasa_response1,
            process_nasa_response2,
            process_nasa_response3,
            process_nasa_response4,
            process_nasa_response5,
            process_nasa_response6,
        ]

        good_passed = False

        print()
        try:
            self._test_processnasaresponse(process_nasa_response_good)
            print('process_nasa_response: Passed the good function!')
            good_passed = True
        except: # pylint: disable=bare-except
            print('process_nasa_response: Failed the good function :(')

        if good_passed:

            caught: int = 0

            for f in bad_f:
                try:
                    self._test_processnasaresponse(f)
                except: # pylint: disable=bare-except
                    caught += 1

            print(f'process_nasa_response: caught {caught}/{len(bad_f)}')

##############################

if __name__ == "__main__":
    unittest.main()
