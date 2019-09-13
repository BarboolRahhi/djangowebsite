from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from blog.models import BlogPost



def detail_blog_view(request, slug):

	context = {}
	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post

	return render(request, 'blog/detail_blog.html', context)



def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = BlogPost.objects.filter(
			Q(title__contains=q)|
			Q(body__icontains=q)
			).distinct()
		for post in posts:
			queryset.append(post)

	# create unique set and then convert to list
	return list(set(queryset)) 




