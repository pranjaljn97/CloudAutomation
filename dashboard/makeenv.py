#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
import json
import io
import sys
import os
from dashboard.models import Project
from dashboard.models import Host
from dashboard.models import Ports
from django.conf import settings
import random
from datetime import datetime
import datetime


global nginxport #range(9000-10000)
global varnishport #range(8000-9000)
global sshnginxport #range(1-1000)
global sshvarnishport #range(1000-2000)
global sshredisport #range(4000-5000)
global sshmongoport #range(3000-4000)
global sshsqlport #range(2000-3000)
global mongoport #6000-7000
global sqlport #range(7000-8000)
global redisport #5000-6000
#conatiner flags

global nginxflag
global varnishflag
global redisflag
global mysqlflag
global mongoflag
global mysqlhostcheck
global mongohostcheck


def makeenvfile(myid):
    curr = Project.objects.get(pk=myid)
    pname = curr.project_name

    # curr = Project.objects.get(pk=myid)
    # pname = curr.project_name

    # #flag checking
    # #nginx-php
    # if curr.PHP_VERSION == 'NA':
    #     nginxflag = False
    # else:
    #     nginxflag = True
    # #varnish
    # if curr.varnish_version == 'NA':
    #     varnishflag = False
    # else:
    #     varnishflag = True
    # #mysql
    # if curr.mysql_version == 'NA' or curr.hostIp_mysql != 'NA':
    #     print "no sql"
    #     mysqlflag = False
    # else:
    #     mysqlflag = True
    # #mongo db
    # if curr.mongo_version == 'NA' or curr.hostIp_mysql != 'NA':
    #     print "no mongo"
    #     mongoflag = False
    # else:
    #     mongoflag = True
    # #redis
    # if curr.redis_version == 'NA':
    #     redisflag = False
    # else:
    #     redisflag = True


    

    obj = Ports.objects.all().filter(projectname=pname).filter(ptype='nginx')
    if len(obj) == 0:
                print "in if"
                
                if curr.PHP_VERSION != 'NA':
                        statusn = True
                        randomport = random.randint(9000,10000)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport)):
                                statusn = False
                                randomport = random.randint(9000,10000)
                        if(statusn == True):
                            nginxport = randomport
                            newport = Ports(port = nginxport, status = '0', projectname = pname, ptype = 'nginx')
                            newport.save()
                        else:
                            while(statusn != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport)):
                                        statusn = False
                                        randomport = random.randint(9000,10000)
                                        break
                                    else:
                                        statusn = True
                                    

                            if(statusn == True):       
                                nginxport = randomport
                                newport = Ports(port = nginxport, status = '0', projectname = pname, ptype = 'nginx')
                                newport.save()

                        sshn = True
                        randomport = random.randint(1,999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport) or str(randomport) == '22' or str(randomport) == '80'):
                                sshn = False
                                randomport = random.randint(1,999)
                        if(sshn == True):
                            sshnginxport = randomport
                            newport = Ports(port = sshnginxport, status = '0', projectname = pname, ptype = 'nginx ssh')
                            newport.save()
                        else:
                            while(sshn != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport) or str(randomport) == '22' or str(randomport) == '80'):
                                        sshn = False
                                        randomport = random.randint(1,999)
                                        break
                                    else:
                                        sshn = True
                                    

                            if(sshn == True):       
                                sshnginxport = randomport
                                newport = Ports(port = sshnginxport, status = '0', projectname = pname, ptype = 'nginx ssh')
                                newport.save()







                # while(statusn != False):
                #     allports = Ports.objects.all()
                #     for oneport in allports:
                #         if(oneport.port == str(randomport)):
                #             statusn = False
                #             randomport = random.randint(9000,10000)
                #     if(statusn == False):
                #         nginxport = randomport
                #         newport = Ports(port = nginxport, status = '0', projectname = pname, ptype = 'nginx')
                #         newport.save()
                #         break

                if curr.varnish_version != 'NA':
                        statusv = True
                        randomport = random.randint(8000,8999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport) or str(randomport) == '8080'):
                                statusv = False
                                randomport = random.randint(8000,8999)
                        if(statusv == True):
                            varnishport = randomport
                            newport = Ports(port = varnishport, status = '0', projectname = pname, ptype = 'varnish')
                            newport.save()
                        else:
                            while(statusv != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport) or str(randomport) == '8080'):
                                        statusv = False
                                        randomport = random.randint(8000,8999)
                                        break
                                    else:
                                        statusv = True
                                    

                            if(statusv == True):       
                                varnishport = randomport
                                newport = Ports(port = varnishport, status = '0', projectname = pname, ptype = 'varnish')
                                newport.save()

                        sshv = True
                        randomport = random.randint(1000,1999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport)):
                                sshv = False
                                randomport = random.randint(1000,1999)
                        if(sshv == True):
                            sshvarnishport = randomport
                            newport = Ports(port = sshvarnishport, status = '0', projectname = pname, ptype = 'varnish ssh')
                            newport.save()
                        else:
                            while(sshv != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport)):
                                        sshv = False
                                        randomport = random.randint(1000,1999)
                                        break
                                    else:
                                        sshv = True
                                    

                            if(sshv == True):       
                                sshvarnishport = randomport
                                newport = Ports(port = sshvarnishport, status = '0', projectname = pname, ptype = 'varnish ssh')
                                newport.save()

                        

                        
                if curr.mysql_version != 'NA' and curr.legacy1 == 'No':    
                        statusmy = True
                        randomport = random.randint(7000,7999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport)):
                                statusmy = False
                                randomport = random.randint(7000,7999)
                        if(statusmy == True):
                            sqlport = randomport
                            newport = Ports(port = sqlport, status = '0', projectname = pname, ptype = 'mysql')
                            newport.save()
                        else:
                            while(statusmy != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport)):
                                        statusmy = False
                                        randomport = random.randint(7000,7999)
                                        break
                                    else:
                                        statusmy = True
                                    

                            if(statusmy == True):       
                                sqlport = randomport
                                newport = Ports(port = sqlport, status = '0', projectname = pname, ptype = 'mysql')
                                newport.save()
                        
                        sshmy = True
                        randomport = random.randint(2000,2999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport) or str(randomport) == '2735'):
                                sshmy = False
                                randomport = random.randint(2000,2999)
                        if(sshmy == True):
                            sshsqlport = randomport
                            newport = Ports(port = sshsqlport, status = '0', projectname = pname, ptype = 'mysql ssh')
                            newport.save()
                        else:
                            while(sshmy != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport) or str(randomport) == '2735'):
                                        sshmy = False
                                        randomport = random.randint(2000,2999)
                                        break
                                    else:
                                        sshmy = True
                                    

                            if(sshmy == True):       
                                sshsqlport = randomport
                                newport = Ports(port = sshsqlport, status = '0', projectname = pname, ptype = 'mysql ssh')
                                newport.save()


                
                if curr.mongo_version != 'NA':
                        statusmo = True
                        randomport = random.randint(6000,6999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport) or str(randomport) == '6379'):
                                statusmo = False
                                randomport = random.randint(6000,6999)
                        if(statusmo == True):
                            mongoport = randomport
                            newport = Ports(port = mongoport, status = '0', projectname = pname, ptype = 'mongo db')
                            newport.save()
                        else:
                            while(statusmo != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport) or str(randomport) == '6379'):
                                        statusmo = False
                                        randomport = random.randint(6000,6999)
                                        break
                                    else:
                                        statusmo = True
                                    

                            if(statusmo == True):       
                                mongoport = randomport
                                newport = Ports(port = mongoport, status = '0', projectname = pname, ptype = 'mongo db')
                                newport.save()

                        sshmo = True
                        randomport = random.randint(3000,3999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport) or str(randomport) == '3306'):
                                sshmo = False
                                randomport = random.randint(3000,3999)
                        if(sshmo == True):
                            sshmongoport = randomport
                            newport = Ports(port = sshmongoport, status = '0', projectname = pname, ptype = 'mongo db ssh')
                            newport.save()
                        else:
                            while(sshmo != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport) or str(randomport) == '3306'):
                                        sshmo = False
                                        randomport = random.randint(3000,3999)
                                        break
                                    else:
                                        sshmo = True
                                    

                            if(sshmo == True):       
                                sshmongoport = randomport
                                newport = Ports(port = sshmongoport, status = '0', projectname = pname, ptype = 'mongo db ssh')
                                newport.save()
                
                if curr.redis_version != 'NA':
                        statusr = True
                        randomport = random.randint(5000,5999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport)):
                                statusr = False
                                randomport = random.randint(5000,5999)
                        if(statusr == True):
                            redisport = randomport
                            newport = Ports(port = redisport, status = '0', projectname = pname, ptype = 'redis')
                            newport.save()
                        else:
                            while(statusr != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport)):
                                        statusr = False
                                        randomport = random.randint(5000,5999)
                                        break
                                    else:
                                        statusr = True
                                    

                            if(statusr == True):       
                                redisport = randomport
                                newport = Ports(port = redisport, status = '0', projectname = pname, ptype = 'redis')
                                newport.save()
                        
                        sshr = True
                        randomport = random.randint(4000,4999)
                        allports = Ports.objects.all()
                        for oneport in allports:
                            if(oneport.port == str(randomport)):
                                sshr = False
                                randomport = random.randint(4000,4999)
                        if(sshr == True):
                            sshredisport = randomport
                            newport = Ports(port = sshredisport, status = '0', projectname = pname, ptype = 'redis ssh')
                            newport.save()
                        else:
                            while(sshr != True):
                                for oneport in allports:
                                    if(oneport.port == str(randomport)):
                                        sshr = False
                                        randomport = random.randint(4000,4999)
                                        break
                                    else:
                                        sshr = True
                                    

                            if(sshr == True):       
                                sshredisport = randomport
                                newport = Ports(port = sshredisport, status = '0', projectname = pname, ptype = 'redis ssh')
                                newport.save()


                
    else:
        print("in else")
        for o1 in obj:
            print("nginx")
            print(o1.port)
            nginxport = o1.port
            obj2 = Ports.objects.all().filter(projectname=pname).filter(ptype='varnish')
            print("varnish")
            for o2 in obj2:
                varnishport = o2.port
                print o2.port
                
            print("nginx ssh")
            obj3 = Ports.objects.all().filter(projectname=pname).filter(ptype='nginx ssh')
            for o3 in obj3:
                sshnginxport = o3.port
                print o3.port
		        
            print("mysql")
            obj4 = Ports.objects.all().filter(projectname=pname).filter(ptype='mysql')
            for o4 in obj4:
                sqlport = o4.port
                print o4.port

            print("mongo")
            obj5 = Ports.objects.all().filter(projectname=pname).filter(ptype='mongo db')
            for o5 in obj5:
                print(o5.port)
                mongoport = o5.port
                
            print("redis")
            obj6 = Ports.objects.all().filter(projectname=pname).filter(ptype='redis')
            for o6 in obj6:
                print(o6.port)
                redisport = o6.port
                 
            print("varnish ssh")
            obj7 = Ports.objects.all().filter(projectname=pname).filter(ptype='varnish ssh')
            for o7 in obj7:
                print(o7.port)
                sshvarnishport = o7.port
                
            print("mysql ssh")
            obj8 = Ports.objects.all().filter(projectname=pname).filter(ptype='mysql ssh')
            for o8 in obj8:
                print(o8.port)
                sshsqlport = o8.port
                
            print("mongo ssh")
            obj9 = Ports.objects.all().filter(projectname=pname).filter(ptype='mongo db ssh')
            for o9 in obj9:
                print(o9.port)
                sshmongoport = o9.port
                
            print("redis ssh")
            obj10 = Ports.objects.all().filter(projectname=pname).filter(ptype='redis ssh')
            for o10 in obj10:
                print(o10.port)
                sshredisport = o10.port
    

    

    #flag checking
    #nginx-php
    if curr.PHP_VERSION == 'NA':
        nginxflag = False
        nginxport = 'false'
        sshnginxport = 'false'
        newport = Ports(port = nginxport, status = '0', projectname = pname, ptype = 'nginx')
        newport.save()
        newport1 = Ports(port = sshnginxport, status = '0', projectname = pname, ptype = 'nginx ssh')
        newport1.save()

    else:
        nginxflag = True
    #varnish
    if curr.varnish_version == 'NA':
        varnishflag = False
        varnishport = 'false'
        sshvarnishport = 'false'
        newport = Ports(port = varnishport, status = '0', projectname = pname, ptype = 'varnish')
        newport.save()
        newport1 = Ports(port = sshvarnishport, status = '0', projectname = pname, ptype = 'varnish ssh')
        newport1.save()
    else:
        varnishflag = True
    #mysql
    if curr.mysql_version == 'NA' or curr.hostIp_mysql != 'NA':
        newip = curr.hostIp_mysql
        hosts = Host.objects.all()
        mysqlflag = False
       
            
        sqlport = 'false'
        sshsqlport = 'false'
        newport = Ports(port = sqlport, status = '0', projectname = pname, ptype = 'mysql')
        newport.save()
        newport1 = Ports(port = sshsqlport, status = '0', projectname = pname, ptype = 'mysql ssh')
        newport1.save()
        
    else:
        mysqlflag = True
    #mongo db
    if curr.mongo_version == 'NA' or curr.hostIp_mysql != 'NA':
        newip = curr.hostIp_mysql
        hosts = Host.objects.all()
        mongoflag = False
        
        mongoport = 'false'
        sshmongoport = 'false'
        newport = Ports(port = mongoport, status = '0', projectname = pname, ptype = 'mongo db')
        newport.save()
        newport = Ports(port = sshmongoport, status = '0', projectname = pname, ptype = 'mongo db ssh')
        newport.save()
        # else:
        #     mongoflag = True
    else:
        mongoflag = True
    #redis
    if curr.redis_version == 'NA':
        redisflag = False
        redisport = 'false'
        sshredisport = 'false'
        newport = Ports(port = redisport, status = '0', projectname = pname, ptype = 'redis')
        newport.save()
        newport = Ports(port = sshredisport, status = '0', projectname = pname, ptype = 'redis ssh')
        newport.save()
    else:
        redisflag = True
        


      
    currpost = Project.objects.get(pk=myid)
    projectname = currpost.project_name
    appname = currpost.application_name
  
    destpath = settings.ENVFILE_PATH + projectname + '_' + appname + '/'
    if not os.path.exists(destpath):
        os.makedirs(destpath)
    print destpath

    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    
    post = Project.objects.get(pk=myid)

    phpVersion  = post.PHP_VERSION
    mysqlVersion = post.mysql_version
    mongoVersion = post.mongo_version
    varnishVersion = post.varnish_version
    redisVersion = post.redis_version

    name = 'dashboard/version.json'
    with open(name, 'r') as f:
        play = json.load(f)
    phpImage = str(play["nginx_php"]["version"][phpVersion])
    mysqlImage = str(play["mysql"]["version"][mysqlVersion])
    mongoImage = str(play["mongodb"]["version"][mongoVersion])
    varnishImage = str(play["varnish"]["version"][varnishVersion])
    redisImage = str(play["redis"]["version"][redisVersion])


    fileopp = 'true'
    if post.total == '0':
        fileopp = 'false'

    pathdir = "documents/" + post.project_name 
    env_path = 'false'
    destpath1 = settings.ENVFILE_PATH + 'documents/' + post.project_name + '/'
    env_path = destpath1 + 'extraenv.json'

    gitUrl = post.git_url
    gitBranch = post.git_branch

    if gitUrl == "":
        gitUrl = "github.com/pranjaljn97/AChecker"
	print("hi admin")
    if gitBranch == "":
        gitBranch = "master"

    data = {'user': {'id': post.id,
                        'USERNAME': post.requester,
                        'project_name': post.project_name,
                        'application_name': post.application_name,
                        'repo_type': post.repo_type,
                        'GITHUB_URL': gitUrl,
                        'GITHUB_USERNAME': post.git_username,
                        'GITHUB_TOKEN': post.git_token,
                        'GITHUB_BRANCH': gitBranch,
                        'envtype': post.envtype,
                        'platform': post.platform,
			'datetime': datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
                        'hostip': post.hostIp },

            'nginx_php': { 'enable': nginxflag,
                            'image': phpImage,
                            'env_file': fileopp,
                            'env_path': env_path,
                            'envi': {
                            'PHP_VERSION': post.PHP_VERSION,
                            'PHP_MODULES': post.PHP_MODULES,
                            'WEB_DOCUMENT_ROOT': post.NGINX_SERVER_ROOT_VALUE,
                            
                            },

                            'volumes': {

                            },
                            'ports': nginxport,
                            'sshport': sshnginxport},
            'mysql' : { 'enable': mysqlflag,
                        'image': mysqlImage,
                        'envi': {
                            'mysql_version': post.mysql_version,
                            'MYSQL_CLIENT_DEFAULT_CHARACTER_SET': post.MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE,
                            'MYSQL_DATABASE': post.MYSQL_DATABASE_NAME_VALUE,                                     
                            
                            'MYSQL_PASSWORD': post.MYSQL_PASSWORD_VALUE,            
                            
                            'MYSQL_ROOT_PASSWORD': post.MYSQL_ROOT_PASSWORD_VALUE,
                            'MYSQL_USER': post.MYSQL_USER_NAME_VALUE,
            },
                            'volumes': {
                                
                            },
                            'ports': sqlport,
                            'sshport': sshsqlport
                            },
                        
            "mongodb": { 'enable': mongoflag,
                          'image': mongoImage,
                            'envi': {
                            'MONGO_INITDB_DATABASE': post.MONGO_INITDB_DATABASE_VALUE,
                            'MONGO_INITDB_ROOT_USERNAME': post.MONGO_INITDB_ROOT_USERNAME_VALUE,
                            'MONGO_INITDB_ROOT_PASSWORD': post.MONGO_INITDB_ROOT_PASSWORD_VALUE,
                            'mongo_version': post.mongo_version,
            },
                            'volumes': {
                                
                            },
                            'ports': mongoport,
                            'sshport': sshmongoport
                        },
                        
            'varnish' : {
                            'enable': varnishflag,
                            'image': varnishImage,
                            'envi': {
                            'VARNISH_BACKEND_HOST': projectname+'_nginx_php',
                            'VARNISH_BACKEND_PORT': post.VARNISH_BACKEND_PORT_VALUE,
                            'VARNISH_PORT_VALUE': post.VARNISH_PORT_VALUE,
                            'varnish_version': post.varnish_version},
                            'volumes': {
                                
                            },
                            'ports': varnishport,
                            'sshport': sshvarnishport
                        
                        },

                            
            'redis' : {
                        'enable': redisflag,
                        'image': redisImage,
                            'envi': {
                            'REDIS_PASSWORD': post.REDIS_PASSWORD_VALUE,
                            'REDIS_LOGFILE': '/home/redis.log' ,
                            'redis_version': post.redis_version },
                            'volumes': {
                                
                            },
                            'ports': redisport,
                            'sshport': sshredisport
                            
                        }}

    

                        

# Write JSON file
    with io.open(post.project_name+ '_' + str(post.id)+'_latest.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
        filecurrpath = "./" + post.project_name + '_' + str(post.id) + '_latest.json'
        filename = post.project_name + '_' + str(post.id) + '_latest.json'
        print destpath + filename
        os.rename(filecurrpath, destpath + filename)
   
    a = destpath + filename
    b = destpath + post.project_name + '_' + str(post.id) +'_'+ datetime.datetime.now().strftime("%Y%m%d-%H%M%S") +'_.json'
    with open(a, 'rb') as src, open(b, 'wb') as dst:
     copyfileobj_example(src, dst)
     print("done")
# makeenvfile()

def copyfileobj_example(source, dest, buffer_size=1024*1024):
    """      
    Copy a file from source to dest. source and dest
    must be file-like objects, i.e. any object with a read or
    write method, like for example StringIO.
    """
    while True:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write(copy_buffer)

def makeEnvHost(id):
    post = Host.objects.get(pk=id)
    hostId = post.hostIdentifier
    hostIp2 = post.hostIp
    destpath = settings.ENVFILE_PATH + post.hostIdentifier + '_' + post.hostIp + '/'
    if not os.path.exists(destpath):
        os.makedirs(destpath)
    print destpath

    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
        
    data = {'id': post.id,
            'hostIdentifier': post.hostIdentifier,
            'hostIp': post.hostIp,
            'hostUsername': post.hostUsername,
            'hostPassword': post.hostPassword,
            'hostDocker': post.hostDocker,
            'hostNginx': post.hostNginx,
            'hostMysql': post.hostMysql,
            'hostMongo': post.hostMongo,
            'mysqlUsername': post.mysqlUsername,
            'mysqlPassword': post.mysqlPassword,
            'mongoUsername': post.mongoUsername,
            'mongoPassword': post.mongoPassword,}


    with io.open(post.hostIdentifier+ '_' + str(post.id)+'.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
        filecurrpath = "./" + post.hostIdentifier + '_' + str(post.id) + '.json'
        filename = post.hostIdentifier + '_' + str(post.id) + '.json'
        print destpath + filename
        os.rename(filecurrpath, destpath + filename)

# Read JSON file
    with open(destpath + post.hostIdentifier+ '_' + str(post.id)+'.json') as data_file:
        data_loaded = json.load(data_file)


