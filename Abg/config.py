from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    OWNER_ID = int(getenv("OWNER_ID", "5715764478"))
    LOGGER_ID = getenv("LOGGER_ID", "-1001819078701")
    TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
    DEV_USERS = "5715764478"
    HANDLER = getenv("HANDLER", "/ ! + . $ #").split()

DEV_USER = Config.DEV_USERS
DEVS = list(set([int(Config.OWNER_ID)] + [int(DEV_USER)]))
