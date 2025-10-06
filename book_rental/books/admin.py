from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ("BookName", "BookDescription",)

admin.site.register(Books, BooksAdmin)
# Register your models here.
