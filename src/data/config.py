import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_UI_URL = os.getenv("BASE_UI_URL", "https://www.greencity.cx.ua/#/greenCity/events")
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT_TIMEOUT", 10))
    HEADLESS_MODE = os.getenv("HEADLESS_MODE", "False").lower() in ("true", "1", "t")