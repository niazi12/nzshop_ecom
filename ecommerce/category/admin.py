from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cate_name',)}
    list_display = ('cate_name', 'slug',)
    # list_filter = ('cate_name',)
    search_fields = ('cate_name',)
admin.site.register(Category, CategoryAdmin)