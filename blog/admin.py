from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ("published", "title","created_at")
    list_filter = ["published", "updated_at","author",]
    date_hierarchy = "created_at"
    #list_disply_links =["title"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields= ["title","content"]

admin.site.register(Post, PostAdmin)
