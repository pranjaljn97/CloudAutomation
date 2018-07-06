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
    connection = MySQLdb.connect (host = os.environ['DB_HOST'], user = os.environ['DB_USER'], passwd = os.environ['DB_PASSWORD'], db = os.environ['DB_NAME'])
    cursor = connection.cursor ()
    cursor.execute ("select *  from dashboard_project where id = %s",myid)
    data = cursor.fetchall ()
    destpath = settings.ENVFILE_PATH
    print destpath

    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    for row in data :
        post = Project.objects.get(pk=myid)
 
        data = {'user': {'id': post.id,
                         'USERNAME': post.requester,
                         'project_name': post.project_name,
			             'application_name': post.application_name,
			             'git_url': post.git_url,
			             'envtype': post.envtype,
		       	         'platform': post.platform},

	            'nginx_php': { 'enable': True,
                               'envi': {
                                'PHP_VERSION': post.PHP_VERSION,
			                    'PHP_MODULES': post.PHP_MODULES,
			                    'NGINX_BACKEND_HOST_VALUE': post.NGINX_BACKEND_HOST_VALUE,
                                'NGINX_SERVER_NAME_VALUE': post.NGINX_SERVER_NAME_VALUE,
                                'NGINX_SERVER_ROOT_VALUE': post.NGINX_SERVER_ROOT_VALUE,
                                'NGINX_STATIC_CONTENT_EXPIRES': post.NGINX_STATIC_CONTENT_EXPIRES_VALUE,
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
                                'MYSQL_DUMP_MAX_ALLOWED_PACKET': post.MYSQL_DUMP_MAX_ALLOWED_PACKET,
                                'MYSQL_PASSWORD': post.MYSQL_PASSWORD_VALUE,            
                                'MYSQL_PORT_VALUE': post.MYSQL_PORT_VALUE,
			                    'MYSQL_ROOT_PASSWORD': post.MYSQL_ROOT_PASSWORD_VALUE,
			                    'MYSQL_USER': post.MYSQL_USER_NAME_VALUE},
                                'volumes': {
                                    
                                },
                                'ports': {

                                }
                                },
                           
                "mongodb": { 'enable': True,
                              'envi': {
                                'MONGO_PORT_VALUE': post.MONGO_PORT_VALUE,
			                    'MONGO_INITDB_DATABASE': post.MONGO_INITDB_DATABASE_VALUE,
       			                'MONGO_INITDB_ROOT_USERNAME': post.MONGO_INITDB_ROOT_USERNAME_VALUE,
        		                'MONGO_INITDB_ROOT_PASSWORD': post.MONGO_INITDB_ROOT_PASSWORD_VALUE,
			                    'mongo_version': post.mongo_version},
                                'volumes': {
                                    
                                },
                                'ports': {

                                }
                            },
                            
         		'varnish' : {
                             'enable': True,
                             'envi': {
                                'VARNISH_BACKEND_HOST': post.VARNISH_BACKEND_HOST_VALUE,
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

    print(data == data_loaded)
    cursor.close ()
    connection.close ()
    #sys.exit()


# makeenvfile()
