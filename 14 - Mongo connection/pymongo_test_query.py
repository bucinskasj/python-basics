from pandas import DataFrame
from pymongo_get_database import get_database
dbname = get_database()

collection_name = dbname["user_1_items"]

item_details = collection_name.find()
for item in item_details:
    # This does not give a very readable output
    items_df = DataFrame(item_details)
    print(items_df)
