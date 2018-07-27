import MySQLdb
def buildMysql(host,user,passwd,uname,upwd,udb):
    
    try:
        mydb = MySQLdb.connect(host=host, port=3306,user=user, passwd=passwd)
        print "hello Connection Successfull"
        cursor = mydb.cursor()
        mkuser = uname
        mkpass = upwd
        dbname = udb
        dbcreation = "CREATE DATABASE %s" %(dbname)
        results = cursor.execute(dbcreation)
        print "DB creation returned", results
        creation = "CREATE USER '%s'@'%s' IDENTIFIED BY '%s'" %(mkuser,'%',mkpass)
        results = cursor.execute(creation)
        print "User creation at world", results
        creation = "CREATE USER '%s'@'%s' IDENTIFIED BY '%s'" %(mkuser,'localhost',mkpass)
        results = cursor.execute(creation)
        #print "User creation at local", results
        #mkpass = upwd
        #setpass = "SET PASSWORD FOR '%s'@'%s' = PASSWORD('%s')" %(mkuser, '%', mkpass)
        #results = cursor.execute(setpass)
        #print "Setting of password returned", results
        granting = "GRANT ALL ON %s.* TO '%s'@'%s'" %(dbname, mkuser,'localhost')
        results = cursor.execute(granting)
        print "Granting of privileges localhost", results
        granting = "GRANT ALL ON %s.* TO '%s'@'%s'" %(dbname, mkuser,'%')
        results = cursor.execute(granting)
        print "Granting of privileges wporld", results  
        flushprivilege = "FLUSH PRIVILEGES"  
        results = cursor.execute(flushprivilege)
        print "Flushing", results    
        res = 't'
        return res
    except MySQLdb.Error, e:

        res = 'f'
        print e
        return res

