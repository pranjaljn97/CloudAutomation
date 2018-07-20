import MySQLdb
def buildMysql(host,user,passwd,uname,upwd,udb):
    
    try:
        mydb = MySQLdb.connect(host=host, port=3306,user=user, passwd=passwd)
        print "hello Connection Successfull"
        cursor = mydb.cursor()
        mkuser = uname
        creation = "CREATE USER '%s'@'%s'" %(mkuser,'%')
        results = cursor.execute(creation)
        print "User creation returned", results
        mkpass = upwd
        setpass = "SET PASSWORD FOR '%s'@'%s' = PASSWORD('%s')" %(mkuser, '%', mkpass)
        results = cursor.execute(setpass)
        print "Setting of password returned", results
        dbname = udb
        dbcreation = "CREATE DATABASE %s" %(dbname)
        results = cursor.execute(dbcreation)
        print "DB creation returned", results
        granting = "GRANT ALL ON %s.* TO '%s'@'%s'" %(dbname, mkuser,'%')
        results = cursor.execute(granting)
        print "Granting of privileges returned", results
        granting = "REVOKE ALL PRIVILEGES ON udb.* FROM '%s'@'%s'" %(mkuser, '%')
        results = cursor.execute(granting)
        print "Revoking of privileges returned", results

        res = 't'
        return res
    except MySQLdb.Error, e:

        res = 'f'
        print e
        return res

