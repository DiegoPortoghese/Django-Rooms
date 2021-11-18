from django.contrib import admin
from .models import Room
from .models import RoomService
from .models import RoomImage


class RoomAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Room
    
    list_display = ["__str__", "creation_date"]
    list_filer = ["creation_date"]
    search_fields = ["title", "description"]


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomService)
admin.site.register(RoomImage)
