from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "auhtor",
        "title",
        "status",
        "category",
        "created_date",
        "published_date",
    ]


admin.site.register(Post)
admin.site.register(Category)
