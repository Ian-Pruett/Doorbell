import os

class DefaultConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')