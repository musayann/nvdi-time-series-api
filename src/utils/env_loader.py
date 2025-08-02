import os
from dotenv import load_dotenv

load_dotenv()


def env(key: str, default: str = ""):
    return os.environ.get(key, default)
