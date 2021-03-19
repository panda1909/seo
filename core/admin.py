from django.contrib import admin
from .models import Comments,Comment_Links,Channels

# Register your models here.
class AdminComments(admin.ModelAdmin):
    list_display = ('Comment',)

class AdminComment_Links(admin.ModelAdmin):
    list_display = ('URL',)

class AdminChannels(admin.ModelAdmin):
    list_display = ('URL',)

admin.site.register(Comments,AdminComments)
admin.site.register(Comment_Links,AdminComment_Links)
admin.site.register(Channels,AdminChannels)
