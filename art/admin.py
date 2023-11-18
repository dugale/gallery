from django.contrib import admin
from .models import Art, Artist, Contact, Subscriber

# Register your models here.
class ArtAdmin(admin.ModelAdmin):
    fields = ('ArtistID', 'name', 'image', 'featured')

admin.site.register(Art, ArtAdmin)
admin.site.register(Artist)
admin.site.register(Contact)
admin.site.register(Subscriber)