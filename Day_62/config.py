import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError('SECRET_KEY environment variable is required')

CSV_FILE_PATH = BASE_DIR / 'cafe-data.csv'

COFFEE_CHOICES = [
    ('☕️', '☕️ Poor'),
    ('☕☕', '☕☕ Fair'),
    ('☕☕☕', '☕☕☕ Good'),
    ('☕☕☕☕', '☕☕☕☕ Very Good'),
    ('☕☕☕☕☕', '☕☕☕☕☕ Excellent')
]

WIFI_CHOICES = [
    ('✘', '✘ No Wifi'),
    ('💪', '💪 Weak'),
    ('💪💪', '💪💪 Fair'),
    ('💪💪💪', '💪💪💪 Good'),
    ('💪💪💪💪', '💪💪💪💪 Strong'),
    ('💪💪💪💪💪', '💪💪💪💪💪 Excellent')
]

POWER_CHOICES = [
    ('✘', '✘ No Power'),
    ('🔌', '🔌 Few Outlets'),
    ('🔌🔌', '🔌🔌 Some Outlets'),
    ('🔌🔌🔌', '🔌🔌🔌 Good Outlets'),
    ('🔌🔌🔌🔌', '🔌🔌🔌🔌 Many Outlets'),
    ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌 Excellent Outlets')
]