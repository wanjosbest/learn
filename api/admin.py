from django.contrib import admin
from .models import Post,category

class PostAdmin(admin.ModelAdmin):
    list_display=("title","content",)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)

admin.site.register(category)
