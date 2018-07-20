from pymongo import MongoClient
def buildMongo(rootuser, rootpass, rootdb, uname, upwd, udb, hostip):
    client = MongoClient(hostip,27017)
    # print  "'" + hostip + ':27017' + "'"
    client.admin.authenticate(rootuser, rootpass)
    db = client[udb]
    client[udb].add_user(uname,upwd, roles=[{'role':'readWrite','db':udb}])
