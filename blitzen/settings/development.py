from decouple import config
from blitzen.settings.common import *


SECRET_KEY = config('DJANGO_SECRET_KEY', '')
