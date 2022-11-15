from django.contrib import admin
from .models import Data_alumni, Dosen, User, GeeksModel

class Data_alumniA(admin.ModelAdmin):
    # ...
    list_display = ('nama_lengkap', 'tahun_masuk')

admin.site.register(Data_alumni, Data_alumniA)
admin.site.register(Dosen)
#admin.site.register(User)
#admin.site.register(GeeksModel)


# Register your models here.
