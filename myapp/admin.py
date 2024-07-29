from django.contrib import admin

from myapp.models import Catalog, Book, Author 

# Register your models here.
admin.site.register(Catalog)
admin.site.register(Book)
admin.site.register(Author)