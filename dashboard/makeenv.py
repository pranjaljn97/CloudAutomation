#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
import json
import io
import MySQLdb
import sys

def makeenvfile(myid):
    connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "mehta123", db = "myproject")
    cursor = connection.cursor ()
    cursor.execute ("select *  from dashboard_project where id = %s",myid)
    data = cursor.fetchall ()

    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    for row in data :
 
        data = {'user': {'id': row[0],
                         'USERNAME': row[1],
                         'project_name':row[4],
			             'application_name':row[5],
			             'git_url':row[6],
			             'envtype':row[3],
		       	         'platform':row[2]},

	            'nginx_php': { 'enable': True,
                             'PHP_VERSION':row[9],
			                 'PHP_MODULES':row[10],
			                 'NGINX_BACKEND_HOST_VALUE':row[11],
                             'NGINX_SERVER_NAME_VALUE': row[12],
                            'NGINX_SERVER_ROOT_VALUE':row[13],
                            'NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE':row[14],                      
                            'NGINX_STATIC_CONTENT_EXPIRES_VALUE':row[15],
                            'NGINX_DRUPAL_FILE_PROXY_URL_VALUE':row[16]},
	            'mysql' : {  'enable': True,
                            'mysql_version':row[22],
 		       	            'MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE':row[28],
                            'MYSQL_DATABASE':row[23],                                     
                            'MYSQL_DUMP_MAX_ALLOWED_PACKET':row[29],
                            'MYSQL_PASSWORD':row[26],            
                            'MYSQL_PORT_VALUE':row[27],
			                'MYSQL_ROOT_PASSWORD':row[24],
			                'MYSQL_USER':row[25]},
                "mongodb": { 'enable': True,
         		             'MONGO_PORT_VALUE': row[17],
			                 'MONGO_INITDB_DATABASE_VALUE': row[18],
       			             'MONGO_INITDB_ROOT_USERNAME': row[19],
        		             'MONGO_INITDB_ROOT_PASSWORD': row[20],
			                'mongo_version': row[21],},
	            'varnish' : {
                             'enable': True,
                             'VARNISH_BACKEND_HOST':row[31],
                             'VARNISH_BACKEND_PORT':row[32],
                             'VARNISH_PORT_VALUE':row[33],
			                 'varnish_version':row[30]},
	            'redis' : {
                            'enable': True,
			                'REDIS_PASSWORD':row[35],
			                'redis_version':row[34], }}

# Write JSON file
        with io.open('data'+str(row[0])+'.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))

# Read JSON file
        with open('data'+str(row[0])+'.json') as data_file:
            data_loaded = json.load(data_file)

    print(data == data_loaded)
    cursor.close ()
    connection.close ()
    #sys.exit()


# makeenvfile()
