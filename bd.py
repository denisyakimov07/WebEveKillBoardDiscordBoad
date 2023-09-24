import pymongo

from environment import get_env

client = pymongo.MongoClient(str(get_env().DATA_BASE_URL))