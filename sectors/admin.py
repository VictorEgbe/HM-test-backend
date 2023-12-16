from django.contrib import admin

from django.contrib.auth.models import User as d_User, Group
from .models import User, Sector, SectorHeading

admin.site.unregister(Group)
admin.site.unregister(d_User)
admin.site.register(User)
admin.site.register(SectorHeading)
admin.site.register(Sector)
