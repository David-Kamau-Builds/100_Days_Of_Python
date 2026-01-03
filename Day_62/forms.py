from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, ValidationError, Regexp
import re
from config import COFFEE_CHOICES, WIFI_CHOICES, POWER_CHOICES


def validate_time_format(form, field):
    """Custom validator for time format (e.g., 8AM, 5:30PM)"""
    time_pattern = r'^(1[0-2]|[1-9])(:?[0-5][0-9])?\s?(AM|PM)$'
    if not re.match(time_pattern, field.data.upper()):
        raise ValidationError('Time must be in format like 8AM or 5:30PM')


def validate_no_csv_injection(form, field):
    """Prevent CSV injection attacks"""
    dangerous_chars = ['=', '+', '-', '@', '\t', '\r', '\n']
    if any(field.data.startswith(char) for char in dangerous_chars):
        raise ValidationError('Invalid characters detected')


class CafeForm(FlaskForm):
    cafe = StringField(
        'Cafe Name', 
        validators=[DataRequired(message='Cafe name is required'), validate_no_csv_injection],
        render_kw={'placeholder': 'Enter the cafe name'}
    )
    location = StringField(
        'Google Maps URL', 
        validators=[
            DataRequired(message='Location URL is required'), 
            URL(message='Please enter a valid URL'),
            validate_no_csv_injection
        ],
        render_kw={'placeholder': 'https://goo.gl/maps/...'}
    )
    open_time = StringField(
        'Opening Time', 
        validators=[
            DataRequired(message='Opening time is required'), 
            validate_time_format,
            validate_no_csv_injection
        ],
        render_kw={'placeholder': 'e.g., 8AM or 7:30AM'}
    )
    close_time = StringField(
        'Closing Time', 
        validators=[
            DataRequired(message='Closing time is required'), 
            validate_time_format,
            validate_no_csv_injection
        ],
        render_kw={'placeholder': 'e.g., 5PM or 5:30PM'}
    )
    coffee_rating = SelectField(
        'Coffee Quality Rating', 
        choices=COFFEE_CHOICES, 
        validators=[DataRequired(message='Please rate the coffee quality')]
    )
    wifi_strength = SelectField(
        'WiFi Strength Rating', 
        choices=WIFI_CHOICES, 
        validators=[DataRequired(message='Please rate the WiFi strength')]
    )
    power_socket = SelectField(
        'Power Socket Availability', 
        choices=POWER_CHOICES, 
        validators=[DataRequired(message='Please rate the power socket availability')]
    )
    submit = SubmitField('Add Cafe')