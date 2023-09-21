from django import template
from datetime import datetime

register = template.Library()

# Created variables to help read the code
DATE_FORMAT_OUTPUT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT_INPUT = "%Y-%m-%dT%H:%M:%S"

@register.filter
def l2l_dt(date):
    if isinstance(date, (str, datetime)): # Check both expected data types
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, DATE_FORMAT_INPUT)
            except ValueError as e: # Throw an error if the string doesn't apply to the format
                raise ValueError(f'Invalid date string format. Expected format: {DATE_FORMAT_INPUT}')
        return date.strftime(DATE_FORMAT_OUTPUT)
    else: # Throw an error if the string doesn't apply to the format
        raise ValueError('Invalid input type for l2l_dt filter. Only accepts a string or datetime object.')