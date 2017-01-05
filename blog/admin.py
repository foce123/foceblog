from django.contrib import admin
from .models import Category,Tag,Blog,Author

# Register your models here.

admin.site.register([Blog,Category,Tag,Author])
