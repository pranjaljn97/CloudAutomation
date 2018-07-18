import MySQLdb
def buildMysql(host,user,passwd,uname,upwd,udb):
    host = 'localhost'
    mydb = MySQLdb.connect(host=host, port=3306,user=user, passwd=passwd)
    print "hello Connection Successfull"
    cursor = mydb.cursor()
    try:
        mkuser = uname
        creation = "CREATE USER '%s'@'%s'" %(mkuser, host)
        results = cursor.execute(creation)
        print "User creation returned", results
        mkpass = upwd
        setpass = "SET PASSWORD FOR '%s'@'%s' = PASSWORD('%s')" %(mkuser, host, mkpass)
        results = cursor.execute(setpass)
        print "Setting of password returned", results
        dbname = udb
        dbcreation = "CREATE DATABASE '%s'@'%s'" %(dbname, host)
        results = cursor.execute(dbcreation)
        print "DB creation returned", results
        granting = "GRANT ALL ON udb.* TO '%s'@'%s'" %(mkuser, host)
        results = cursor.execute(granting)
        print "Granting of privileges returned", results
        granting = "REVOKE ALL PRIVILEGES ON udb.* FROM '%s'@'%s'" %(mkuser, host)
        results = cursor.execute(granting)
        print "Revoking of privileges returned", results
    except MySQLdb.Error, e:
        print e
