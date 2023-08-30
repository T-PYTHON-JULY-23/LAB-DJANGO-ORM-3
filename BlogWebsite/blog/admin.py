from django.contrib import admin
from django.contrib import admin
from .models import Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','category' ,'publish_date')
    list_filter = ('title','category',)


class CommenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('content_comment',)





admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommenAdmin)