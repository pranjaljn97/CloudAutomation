from pymongo import MongoClient
def buildMongo(uname,upwd,udb):
    client = MongoClient('localhost:27017')   
    client.admin.authenticate('root', '1234')
    db = client[udb]
    client.testdb.add_user(uname,upwd, roles=[{'role':'readWrite','db':db}])