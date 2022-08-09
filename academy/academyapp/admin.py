from django.contrib import admin
from .models import CategoryLevelOne, CategoryLevelTwo, Course

# Register your models here.


class CategoryLevelOneAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'order_number', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('category_name',)


class CategoryLevelTwoAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'order_number', 'slug', 'sub_category')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('category_name',)
    list_filter = ('sub_category',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'unit_price', 'slug',
                    'instructor', 'category_level_two')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'instructor', 'category_level_two')


admin.site.register(CategoryLevelOne, CategoryLevelOneAdmin)
admin.site.register(CategoryLevelTwo, CategoryLevelTwoAdmin)
admin.site.register(Course, CourseAdmin)
