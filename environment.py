import logging

from dotenv import load_dotenv
import os

load_dotenv(verbose=True)


class _Environment:
    DISCORD_BOT_TOKEN: str
    BASE_URL: str


    def __init__(self):
        self.DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
        self.DATA_BASE_URL = os.getenv('DATA_BASE_URL')


    @staticmethod
    def __parse_log_level(log_level_str: str) -> int:
        switcher = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL,
        }
        return switcher.get(log_level_str, logging.INFO)

    def __str__(self):
        return f'DISCORD_BOT_TOKEN={self.DISCORD_BOT_TOKEN}\nDISCORD_CLIENT_ID={self.DISCORD_CLIENT_ID}'


__environment = _Environment()


def get_env():
    return __environment