import os

EMAIL_DOMAIN = "example.com"
SLACK_TOKEN = "yourtoken"
SLACK_CHANNEL = "#general"
SHELVE_FILE = "meetings.shelve"
ATTENDANCE_TIME_LIMIT = 60 * 15
PAIRING_SIZE = 2

if os.path.exists('config_private.py'):
    # Use config_private for your own personal settings - default to be git ignored.
    # Yup, intentionally using wildcard import to shadow the default values
    from config_private import *
