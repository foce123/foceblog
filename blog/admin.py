from django.contrib import admin
from .models import Category,Tag,Blog,Author

# Register your models here.

class Media:
	js=(
		'/static/js/tinymce/tiny_mce.min.js',
	)

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','author','created','category','tags',)

admin.site.register([Blog,Category,Tag,Author])
