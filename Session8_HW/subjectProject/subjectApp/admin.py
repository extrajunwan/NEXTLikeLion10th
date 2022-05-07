from django.contrib import admin
from .models import Major, Subject
# Register your models here.
class MajorAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name', )}

admin.site.register(Major, MajorAdmin)
admin.site.register(Subject)


