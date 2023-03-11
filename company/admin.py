from django.contrib import admin
from .models import Post, ProductDemo, Contact, Book
from django_summernote.admin import SummernoteModelAdmin #ep5 week6

class ModelAdmin(SummernoteModelAdmin): #ep5 week6
    summernote_fields = ('body',)
    list_display = ['title', 'date_created', 'date_updated']

# Register your models here.

#admin.site.register(Model, ModelAdmin)

admin.site.register(Post, ModelAdmin) #ModelAdmin added ep5
admin.site.register(ProductDemo)
admin.site.register(Contact)
admin.site.register(Book)




