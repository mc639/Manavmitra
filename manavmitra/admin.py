from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Blog, Epaper, Trailer

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Epaper,)
admin.site.register(Trailer)




