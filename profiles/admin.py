from django.contrib import admin
from profiles.models import Userprofile
# Register your models here.
class UserprofileAdmin(admin.ModelAdmin):
	
	class Meta:
		model = Userprofile

admin.site.register(Userprofile, UserprofileAdmin)