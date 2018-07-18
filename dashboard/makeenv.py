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
global nginxport
global varnishport
global sshnginxhport
global mongoport
global sqlport


def makeenvfile(myid):



    curr = Project.objects.get(pk=myid)
    pname = curr.project_name
    

    obj = Ports.objects.all().filter(projectname=pname).filter(ptype='nginx')
    if len(obj) == 0:
                statusn = False
                randomport = random.randint(9000,10000)
                while(statusn == False):
                    allports = Ports.objects.all()
                    for oneport in allports:
                        if(oneport.port == str(randomport)):
                            statusn = False
                            randomport = random.randint(9000,10000)
                    if(statusn == False):
                        nginxport = randomport
                        newport = Ports(port = nginxport, status = '0', projectname = pname, ptype = 'nginx')
                        newport.save()
                        break

                statusmy = False
                randomport = random.randint(8000,8999)
                while(statusmy == False):
                    allports = Ports.objects.all()
                    for oneport in allports:
                        if(oneport.port == str(randomport)):
                            statusmy = False
                            randomport = random.randint(8000,8999)
                    if(statusmy == False):
                        varnishport = randomport
                        newport = Ports(port = varnishport, status = '0', projectname = pname, ptype = 'varnish')
                        newport.save()
                        break
                statussh = False
                randomport = random.randint(7000,7999)
                while(statussh == False):
                    allports = Ports.objects.all()
                    for oneport in allports:
                        if(oneport.port == str(randomport)):
                            statussh = False
                            randomport = random.randint(7000,7999)
                    if(statussh == False):
                        sshnginxhport = randomport
                        newport = Ports(port = sshnginxhport, status = '0', projectname = pname, ptype = 'sshport')
                        newport.save()
                        break
                statusql = False
                randomport = random.randint(6000,6999)
                while(statusql == False):
                    allports = Ports.objects.all()
                    for oneport in allports:
                        if(oneport.port == str(randomport)):
                            statusql = False
                            randomport = random.randint(6000,6999)
                    if(statusql == False):
                        sqlport = randomport
                        newport = Ports(port = sqlport, status = '0', projectname = pname, ptype = 'sqlport')
                        newport.save()
                        break
                statumongo = False
                randomport = random.randint(5000,5999)
                while(statumongo == False):
                    allports = Ports.objects.all()
                    for oneport in allports:
                        if(oneport.port == str(randomport)):
                            statumongo = False
                            randomport = random.randint(5000,5999)
                    if(statumongo == False):
                        mongoport = randomport
                        newport = Ports(port = mongoport, status = '0', projectname = pname, ptype = 'mongoport')
                        newport.save()
                        break
                        
                
    else:
        for o1 in obj:
                print(o1.port)
                nginxport = o1.port
                obj2 = Ports.objects.all().filter(projectname=pname).filter(ptype='varnish')
                for o2 in obj2:
                    varnishport = o2.port
		    print("var")
	            print(varnishport)
                obj3 = Ports.objects.all().filter(projectname=pname).filter(ptype='sshport')
                for o3 in obj3:
                    sshnginxhport = o3.port
		    print("ssh")
		    print(sshnginxhport)
                obj4 = Ports.objects.all().filter(projectname=pname).filter(ptype='sqlport')
                for o4 in obj4:
                    sqlport = o4.port
		    print("sql")
                    print(sqlport)
                obj5 = Ports.objects.all().filter(projectname=pname).filter(ptype='mongoport')
                for o5 in obj5:
		    print(o5.port)
                    mongoport = o5.port

      
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


    data = {'user': {'id': post.id,
                        'USERNAME': post.requester,
                        'project_name': post.project_name,
                        'application_name': post.application_name,
                        'repo_type': post.repo_type,
                        'GITHUB_URL': post.git_url,
                        'GITHUB_USERNAME': post.git_username,
                        'GITHUB_TOKEN': post.git_token,
                        'GITHUB_BRANCH': post.git_branch,
                        'envtype': post.envtype,
                        'platform': post.platform,
                        'hostip': post.hostIp },

            'nginx_php': { 'enable': True,
                            'image': phpImage,
                            'envi': {
                            'PHP_VERSION': post.PHP_VERSION,
                            'PHP_MODULES': post.PHP_MODULES,
                            'WEB_DOCUMENT_ROOT': post.NGINX_SERVER_ROOT_VALUE,
                            
                            },

                            'volumes': {

                            },
                            'ports': nginxport,
                            'sshport': sshnginxhport

                            },
            'mysql' : { 'enable': True,
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
                            'ports': '3308',
                            'sqlport': sqlport
                            },
                        
            "mongodb": { 'enable': True,
                          'image': mongoImage,
                            'envi': {
                            'MONGO_INITDB_DATABASE': post.MONGO_INITDB_DATABASE_VALUE,
                            'MONGO_INITDB_ROOT_USERNAME': post.MONGO_INITDB_ROOT_USERNAME_VALUE,
                            'MONGO_INITDB_ROOT_PASSWORD': post.MONGO_INITDB_ROOT_PASSWORD_VALUE,
                            'mongo_version': post.mongo_version,
            },
                            'volumes': {
                                
                            },
                            'ports': '27019',
                            'mongoport': mongoport
                        },
                        
            'varnish' : {
                            'enable': True,
                            'image': varnishImage,
                            'envi': {
                            'VARNISH_BACKEND_HOST': projectname+'_nginx_php',
                            'VARNISH_BACKEND_PORT': post.VARNISH_BACKEND_PORT_VALUE,
                            'VARNISH_PORT_VALUE': post.VARNISH_PORT_VALUE,
                            'varnish_version': post.varnish_version},
                            'volumes': {
                                
                            },
                            'volumes': {
                                
                            },
                            'ports': varnishport
                        
                        },

                            
            'redis' : {
                        'enable': True,
                        'image': redisImage,
                            'envi': {
                            'REDIS_PASSWORD': post.REDIS_PASSWORD_VALUE,
                            'REDIS_LOGFILE': '/home/redis.log' ,
                            'redis_version': post.redis_version },
                            'volumes': {
                                
                            },
                            'ports': {
                                
                            },
                            
                        }}

    

                        

# Write JSON file
    with io.open(post.project_name+ '_' + str(post.id)+'.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
        filecurrpath = "./" + post.project_name + '_' + str(post.id) + '.json'
        filename = post.project_name + '_' + str(post.id) + '.json'
        print destpath + filename
        os.rename(filecurrpath, destpath + filename)

# Read JSON file
    with open(destpath + post.project_name+ '_' + str(post.id)+'.json') as data_file:
        data_loaded = json.load(data_file)


    #sys.exit()


# makeenvfile()



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
            'mysqlPassword': post.mysqlPassword,}


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


