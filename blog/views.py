from django.shortcuts import render,render_to_response
from django.template import RequestContext
from blog.models import Blog, Comment, Author, Category, Tag
from django.http import Http404
from blog.forms import CommentForm

# Create your views here.

def get_blogs(request):
	blog_s = {
		'blog_s': Blog.objects.all().order_by('-created')
	}
	return render(request, 'blog.html', blog_s)

def get_detail(request,blog_id):
	try:
		blog = Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		raise Http404
	
	if request.method == 'GET':
		form = CommentForm()
	else:
		form = CommentForm(request.POST)
		if form.is_valid():
			    cleaned_data = form.cleaned_data
			    cleaned_data['blog'] = blog
			    Comment.objects.create(**cleaned_data)

	detail = {
		'blog': blog,
		'comments': blog.comment_set.all().order_by('-created'),
		'form': form
	}
	return render(request, 'blog-detail.html', detail)

def blog_search(request):
        tags = Tag.objects.all()
        if 'search' in request.GET:
                search = request.GET['search']
                blogse = Blog.objects.filter(title__icontains=search).order_by('-created')
                categories = Category.objects.all()
                return render_to_response('blog-search.html',{"blog_s":blogse,"tags":tags,"categories":categories})
	else:
		blogse = Blog.objects.order_by('-id')
		return render_to_response("blog.html",{"blog_s":blogse, "tags":tags})
