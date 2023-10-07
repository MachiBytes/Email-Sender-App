import os
from dotenv import load_dotenv

load_dotenv()

# Environment Variables
EMAIL = os.getenv("EMAIL")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# App Settings
APP_GEOMETRY = "500x500"
APP_TITLE = "Email Sender"
APP_APPEARANCE_MODE = "dark"  # dark/light/system
