from django.contrib import admin

from .models import Project
from .models import Ports
from .models import runningstack
from .models import Host
from .models import mysqluser
from .models import mongoform

admin.site.register(Project)
admin.site.register(Ports)
admin.site.register(runningstack)
admin.site.register(Host)
admin.site.register(mysqluser)
admin.site.register(mongoform)

