import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
