from django.contrib import admin
from .models import Post, Comment
from .models import MyModel
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(MyModel, MyModelAdmin)