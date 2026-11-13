import configparser
import os

class ConfigReader:
    @staticmethod
    def get_config():
        config = configparser.ConfigParser()
        # to find right path of config.ini
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.ini'))
        config.read(config_path)
        return config

    @classmethod
    def get_base_url(cls):
        return cls.get_config().get('Settings', 'base_url')

    @classmethod
    def get_api_base_url(cls):
        """Read API base URL from config.ini with fallback safety"""
        return cls.get_config().get('Settings', 'api_base_url', fallback="https://jsonplaceholder.typicode.com")

    @classmethod
    def get_browser(cls):
        return cls.get_config().get('Settings', 'browser', fallback="chrome")

    @classmethod
    def get_headless(cls):
        return cls.get_config().get('Settings', 'headless', fallback="false")