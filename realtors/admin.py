from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin): #Son los campos que se muestran en admin al momento de administrar dicha clase
    list_display = ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
