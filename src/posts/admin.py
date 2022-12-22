from django.contrib import admin
from posts.models import BlogPost
# Register your models here.

class BlogPostAdmnin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_update",) #tous ce que nous voullons afficher dans l'interface d' admin
    list_editable = ("published",) #qui permete d'édité certain champ dans l'interface d'admin

admin.site.register(BlogPost, BlogPostAdmnin)