import MySQLdb
def buildMysql(host,user,passwd,uname,upwd,udb):
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
        dbcreation = "CREATE DATABASE %s" %(dbname)
        results = cursor.execute(dbcreation)
        print "DB creation returned", results

 
	dbc2 = "FLUSH PRIVILEGES"
        results = cursor.execute(dbc2)
        print "DB c 2", results



        granting = "GRANT ALL ON %s.* TO '%s'@'%s'" %(udb, mkuser, host)
        results = cursor.execute(granting)
        print "Granting of privileges returned", results
        granting = "REVOKE ALL PRIVILEGES ON %s.* FROM '%s'@'%s'" %(udb,mkuser, host)
        results = cursor.execute(granting)
        print "Revoking of privileges returned", results
    except MySQLdb.Error, e:
        print e
