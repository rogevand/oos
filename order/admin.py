from django.contrib import admin

from .models import Service
from .models import Musician
from .models import Hymn

admin.site.register(Service)
admin.site.register(Musician)
admin.site.register(Hymn)
