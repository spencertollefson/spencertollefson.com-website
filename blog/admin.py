from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    date_hierarchy = 'published_date'
    search_fields = ['title', 'content',]
    list_display = ('title','created_date','published_date', 'type')
    list_filter = ('type',)



#Customizations to Admin site
admin.site.site_header = "spencertollefson.com Admin"
admin.site.site_title = "offlimits!"
admin.site.index_title = ''
