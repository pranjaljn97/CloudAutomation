from pymongo import MongoClient
def buildMongo(rootuser, rootpass, rootdb, uname, upwd, udb):
    client = MongoClient('localhost:27017')   
    client.admin.authenticate(rootuser, rootpass)
    client.db.add_user(uname,upwd, roles=[{'role':'readWrite','db':udb}])
