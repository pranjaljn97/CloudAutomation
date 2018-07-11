#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
import json
import io
import MySQLdb
import sys
import os
from dashboard.models import Project
from django.conf import settings



def makeenvfile(myid):
  
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

    data = {'user': {'id': post.id,
                        'USERNAME': post.requester,
                        'project_name': post.project_name,
                        'application_name': post.application_name,
                        'GITHUB_URL': post.git_url,
                        'GITHUB_USERNAME': post.git_username,
                        'GITHUB_TOKEN': post.git_token,
                        'GITHUB_BRANCH': post.git_branch,
                        'envtype': post.envtype,
                        'platform': post.platform,
                        'hostip': post.hostIp },

            'nginx_php': { 'enable': True,
                            'envi': {
                            'PHP_VERSION': post.PHP_VERSION,
                            'PHP_MODULES': post.PHP_MODULES,
                            'WEB_DOCUMENT_ROOT': post.NGINX_SERVER_ROOT_VALUE,
                            
                            },

                            'volumes': {

                            },
                            'ports': '9000'                                                                                                               
                            },
            'mysql' : { 'enable': True,
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
                            'ports': '3308'
                            },
                        
            "mongodb": { 'enable': True,
                            'envi': {
                            'MONGO_INITDB_DATABASE': post.MONGO_INITDB_DATABASE_VALUE,
                            'MONGO_INITDB_ROOT_USERNAME': post.MONGO_INITDB_ROOT_USERNAME_VALUE,
                            'MONGO_INITDB_ROOT_PASSWORD': post.MONGO_INITDB_ROOT_PASSWORD_VALUE,
                            'mongo_version': post.mongo_version,
            },
                            'volumes': {
                                
                            },
                            'ports': '27019'
                        },
                        
            'varnish' : {
                            'enable': True,
                            'envi': {
                            'VARNISH_BACKEND_HOST': 'nginx_php',
                            'VARNISH_BACKEND_PORT': post.VARNISH_BACKEND_PORT_VALUE,
                            'VARNISH_PORT_VALUE': post.VARNISH_PORT_VALUE,
                            'varnish_version': post.varnish_version},
                            'volumes': {
                                
                            },
                            'volumes': {
                                
                            },
                            'ports': '8085'
                        
                        },

                            
            'redis' : {
                        'enable': True,
                            'envi': {
                            'REDIS_PASSWORD': post.REDIS_PASSWORD_VALUE,
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
