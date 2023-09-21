from django.test import TestCase
from datetime import datetime
from l2l.templatetags.l2l_extras import l2l_dt

class CustomFilterTests(TestCase):
    def setUp(self):
        # Set up test date values and ISO string
        self.valid_datetime = datetime(2023, 9, 20, 15, 30, 45, 123456)
        self.valid_datetime_iso = "2023-09-20T15:30:45"

    def test_formatting_valid_datetime(self):
        # Test if the filter correctly formats a valid datetime object
        formatted_date = l2l_dt(self.valid_datetime)
        self.assertEqual("2023-09-20 15:30:45", formatted_date)

    def test_formatting_valid_datetime_iso(self):
        # Test if the filter correctly formats a valid ISO datetime string
        formatted_date = l2l_dt(self.valid_datetime_iso)
        self.assertEqual("2023-09-20 15:30:45", formatted_date)

    def test_invalid_datetime_input(self):
        # Test if the filter raises a ValueError when an invalid datetime string is provided
        with self.assertRaises(ValueError):
            l2l_dt("InvalidDateFormat")

    def test_non_string_or_datetime_input(self):
        # Test if the filter raises a ValueError for non-string and non-datetime input
        with self.assertRaises(ValueError):
            l2l_dt(00000)

# Knowledge https://docs.djangoproject.com/en/4.2/topics/testing/overview/