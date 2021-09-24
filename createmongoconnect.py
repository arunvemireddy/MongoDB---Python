import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["owner"]

mydict = { "name": "letty", "address": "Highway 34" }

x = mycol.insert_one(mydict)