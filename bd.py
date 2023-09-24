import pymongo
from loguru import logger
from environment import get_env

client = pymongo.MongoClient(str(get_env().DATA_BASE_URL))
db: pymongo.database.Database = client.session_url_tokens

def authentication(cred) -> bool:
    try:
        server = db.session_url_tokens.find_one({'_id': str(cred['s'][0])})
        if server and server['url_token'] == str(cred['t'][0]):
            return True
        else:
            return False
    except Exception as ex:
        logger.error(f"Cant get server info {ex}")

