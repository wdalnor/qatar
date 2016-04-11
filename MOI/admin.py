from django.contrib import admin
from .models import Employee,Tender



class TenderInline(admin.TabularInline):

    model = Tender
    extra = 0



class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('devision','emp_name','emp_phon')

    list_filter = ['devision']
    search_fields = ['emp_name','devision','emp_phon']
  

    inlines = [TenderInline]





admin.site.register(Employee,EmployeeAdmin)
#admin.site.register(Tender)

# Register your models here.
