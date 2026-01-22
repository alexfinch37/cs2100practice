import unittest
from unittest.mock import patch, Mock
from main import (greet_person, is_cold_f, THRESHOLD_TEMP_F)

class TestMainApp(unittest.TestCase):
    @patch('builtins.input', side_effect=['alice'])
    @patch('builtins.print')
    def test_greetperson(self, mock_print: Mock, _: Mock) -> None:
        """
        Say Hello to Alice
        """
        greet_person()
        expected_calls = [
            unittest.mock.call("howdy alice"),
        ]
        mock_print.assert_has_calls(expected_calls)

    def test_is_coldf_70(self) -> None:
        "tests is_cold_f for 70"
        self.assertFalse(is_cold_f(70))
    def test_is_coldf_threshold(self) -> None:
        "tests is_cold_f for thres"
        self.assertFalse(is_cold_f(THRESHOLD_TEMP_F))
    def test_is_coldf_freezing(self) -> None:
        "tests is_cold_f for 32"
        self.assertTrue(is_cold_f(32))
    def test_is_coldf_boiling(self) -> None:
        "tests is_cold_f for 212"
        self.assertFalse(is_cold_f(212))
    def test_is_coldf_belowthres(self) -> None:
        "tests is_cold_f for 212"
        self.assertTrue(is_cold_f(THRESHOLD_TEMP_F-1))

if __name__ == "__main__":
    unittest.main()
