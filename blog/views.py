from django.shortcuts import render
from .models import Blog,Comment
from django.http import Http404
from .forms import CommentForm

# Create your views here.

def get_blogs(request):
	ctx = {
		'blogs': Blog.objects.all().order_by('-created')
	}
	return render(request, 'blog.html', ctx)

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

def test(request):
	return render(request,'blog-base.html')
