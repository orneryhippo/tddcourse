# project/config.py
import os

SECRET_KEY = os.environ.get('SESSION_KEY','hello, kitty') #b'\x98\xe0\xc4;B\xd2Wd\x16\xb1{\x99\x9e\xc9\xd95\xa4\xf1\xe8\xc6\x06L\x99L'

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
