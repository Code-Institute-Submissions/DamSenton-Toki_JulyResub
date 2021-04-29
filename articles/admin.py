from django.contrib import admin
from .models import Articles

# Register your models here.


class ArticlesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'pk',
        'date'
        
    )


admin.site.register(Articles, ArticlesAdmin)
