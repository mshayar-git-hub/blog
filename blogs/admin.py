from django.contrib import admin
from.models import About, Category, Blog, Follow_link

class BlogAdminm(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    search_fields = ('title' , 'category__category_name' , 'author' , 'status')
    list_display = ('title'  ,'category' , 'author' , 'status' , 'is_featured')
    list_editable = ('is_featured',)

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self , request):
        count = About.objects.all().count()
        if count == 0:
            return True
        else: False


# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdminm)
admin.site.register(About, AboutAdmin)
admin.site.register(Follow_link)