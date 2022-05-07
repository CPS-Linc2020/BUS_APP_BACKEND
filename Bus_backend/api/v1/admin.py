from django.contrib import admin
from .models import BusStation
from .models import RoadNode
from .models import BusRoute
from .models import NodeLink

# Register your models here.
# class BusAdmin(admin.ModelAdmin):
#     pass

admin.register(BusStation)
admin.register(RoadNode)
admin.register(BusRoute)
admin.register(NodeLink)
