import json
from django.conf import settings
from .models import Project

def buildinfo(request,id,jsonfile,hostip):
    currpost = Project.objects.get(pk=id)
    projectname = currpost.project_name
    appname = currpost.application_name
    name = settings.ENVFILE_PATH + projectname + '_' + appname + '/hostoutput_latest.json'
    with open(name, 'r') as f:
        plays = json.load(f)
    message = ""
    f2 = open('templates/dashboard/detailform1.html','w')
    for x in plays['plays']:
        #print("Installing Docker Packages:" + str(x['tasks'][9]['hosts']['127.0.0.1']['results'][0]['failed']))
        print("Installing Docker Packages:")
        if (str(x['tasks'][2]['hosts'][hostip]['results'][0]['failed']) == "False"):
            print("True")
            message = message + """{% extends "dashboard/detailformside.html" %}
                         {% block content %}
                                <center>
                               <div class="row">
                            
                               <div class="col-md-12" >
                              
                                <div class="card">
                                 
                                    <div class="header">
                                        
                                        <h5 class="title"><b>Build Details</b></h5>
                                            <br>
                                            


                                            <p class="category"></p>
                                            <br>
                                            
                                            <i class="fa fa-circle text-info"></i> Creating Mysql Directories&nbsp: True <br>"""

          

        else:
                print("False")

        if (str(x['tasks'][2]['hosts'][hostip]['results'][1]['failed']) == "False"):
            print("True")
            message = message + """
                                <i class="fa fa-circle text-info"></i> Creating Mongo Directories &nbsp: True <br>"""
        else:
            print("False")
        print("Creating Mongo Directories:")
        if (str(x['tasks'][2]['hosts'][hostip]['results'][2]['failed']) == "False"):
            print("True")
            print("True")
            message = message + """<i class="fa fa-circle text-info"></i> Creating Code Directories: True <br><br><br><br></div></div></div></div></center>{% endblock %}"""
        else:
            print("False")

                              
        f2.write(message)
        print("wdjwn")
        f2.close()
            
