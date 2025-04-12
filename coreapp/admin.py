from django.contrib import admin
from .models import Guest, RoomType, Room, Lounge, Auditorium, Booking, Payment

# Register your models here.

admin.site.register(Guest)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Lounge)
admin.site.register(Auditorium)
admin.site.register(Booking)
admin.site.register(Payment)