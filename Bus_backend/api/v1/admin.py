from django.contrib import admin
from .models import BusRoute
from .models import BusStation
from .models import NodeLink
from .models import RoadNode

# Register your models here.
# class BusAdmin(admin.ModelAdmin):
#     pass

admin.register(BusStation)
admin.register(RoadNode)
admin.register(BusRoute)
admin.register(NodeLink)
