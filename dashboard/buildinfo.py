import json
def buildinfo(request,id):
    with open('dashboard/123.json', 'r') as f:
        plays = json.load(f)
    message = ""
    f2 = open('templates/dashboard/detailform'+str(id)+'.html','w')
    for x in plays['plays']:
        #print("Installing Docker Packages:" + str(x['tasks'][9]['hosts']['127.0.0.1']['results'][0]['failed']))
        print("Installing Docker Packages:")
        if (str(x['tasks'][1]['hosts']['127.0.0.1']['results'][0]['failed']) == "False"):
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
                                            <i class="fa fa-circle text-info"></i> Installing Docker Packages&nbsp: True <br>"""

          

        else:
                print("False")

        print("Creating Directories:")
        print("Creating MySql Directories:")
        if (str(x['tasks'][9]['hosts']['127.0.0.1']['results'][0]['failed']) == "False"):
            print("True")
            message = message + """
                                <i class="fa fa-circle text-info"></i> Creating MySql Directories &nbsp: True <br>"""
        else:
            print("False")
        print("Creating Mongo Directories:")
        if (str(x['tasks'][9]['hosts']['127.0.0.1']['results'][1]['failed']) == "False"):
            print("True")
            print("True")
            message = message + """<i class="fa fa-circle text-info"></i> Creating Mongo Directories: True <br>"""
        else:
            print("False")
        print("Creating Code Directories:")
        if (str(x['tasks'][9]['hosts']['127.0.0.1']['results'][2]['failed']) == "False"):
            print("True")
            print("True")
            message = message + """<i class="fa fa-circle text-info"></i> Creating Code Directories &nbsp : True <br>"""
        else:
            print("False")
        print("Docker Compose Up:")
        if (str(x['tasks'][12]['hosts']['127.0.0.1']['result']['failed']) == "False"):
            print("True")
            print("True")
            message = message + """<i class="fa fa-circle text-info"></i> Docker Compose Up &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp: True <br><br><br></div></div></div></div></center>{% endblock %}
                              """
            f2.write(message)
            print("wdjwn")
            f2.close()
            
        else:
            print("False")


