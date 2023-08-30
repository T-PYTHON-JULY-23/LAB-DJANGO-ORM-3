from django.contrib import admin
from .models import Recpie
from .models import Comment

# Register your models here.
class RecpieAdmin(admin.ModelAdmin):
    list_display=('title_recipes','category','publish_date')
    list_filter=('category',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('rating','created_at')
    list_filter=('rating',)

admin.site.register(Recpie,RecpieAdmin)
admin.site.register(Comment,CommentAdmin)
