from pymongo import MongoClient
import datetime 
client = MongoClient("mongodb+srv://nayannewdb:nayan123@cluster0.vvqxowq.mongodb.net/")

db=client.scrapy
posts=db.test_collection

# post = {
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.now(tz=datetime.timezone.utc),
# }

# post_id = posts.insert_one(post)
# print(post_id)