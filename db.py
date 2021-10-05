import pymongo
from url import cluster
mongo_client = pymongo.MongoClient(cluster)

def connection():
    try:

        db_list = mongo_client.list_database_names()

        if "company" in db_list:

            my_database = mongo_client['company'];

            collection = my_database.users

            return collection

        else:

            print('no database found...!')

    except Exception:
        print('bad server')
