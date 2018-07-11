from dashboard.models import runningstack
from dashboard.models import Ports
def rstack(posts):
    for post in posts:
   
        projname = post.project_name
        appname = post.application_name
        host = runningstack(projectname=projname)
        host.save()

    for post in posts:
   
        projname = post.project_name
        appname = post.application_name

        url = projname +'-'+ appname +'.tothenew.tk'
        mysqluname = post.MYSQL_USER_NAME_VALUE
        mysqlupwd = post.MYSQL_PASSWORD_VALUE
        mongouname = post.MONGO_INITDB_ROOT_USERNAME_VALUE
        mongoupwd = post.MONGO_INITDB_ROOT_PASSWORD_VALUE
        obj = Ports.objects.all().filter(projectname=projname).filter(ptype='nginx')
        for o1 in obj:
                nginxport = o1.port
                obj2 = Ports.objects.all().filter(projectname=projname).filter(ptype='varnish')
                for o2 in obj2:
                    varnishport = o2.port

        currpost = runningstack.objects.get(projectname=projname)

        currpost.status = 'Approved'
        currpost.url = url
        currpost.urlStatus = 'Check Url Status'
        currpost.hostIp = post.hostIp
        currpost.hostStatus = 'Check Host Status'
        currpost.nginxport = nginxport
        currpost.varnishport = varnishport
        currpost.mysqluname = mysqluname
        currpost.mysqlupwd = mysqlupwd
        currpost.mysqlstatus = 'Check Mysql Status'
        currpost.mongouname = mongouname
        currpost.mongoupwd = mongoupwd
        currpost.mongostatus = 'Check Mongo Status'
        currpost.save()
