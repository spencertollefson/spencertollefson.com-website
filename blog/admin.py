from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    search_fields = ['title', 'content',]
    list_display = ('title','created_date','published_date', 'type')
    list_filter = ('type',)
    prepopulated_fields = {
        "slug": ("title",)
    }



#Customizations to Admin site
admin.site.site_header = "spencertollefson.com top secret"
admin.site.site_title = "offlimits!"
admin.site.index_title = ''
