from django.contrib import admin
from . models import Profile,Editpage,Gallery


class EditpageAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'content')  # Display section name and content in the admin list
    search_fields = ['section_name']  # Allow searching by section name for easier management
# Register your models here.
admin.site.register(Profile)
admin.site.register(Editpage, EditpageAdmin)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')