from dotenv import load_dotenv
from pathlib import Path 
import os

    # PATH TO ENV FILE 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """
    Set config vars 
        from .env
    :param: enviroment filesys
    """

    TESTING = os.getenv('TESTING')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER = os.getenv('SERVER')
    