from django.shortcuts import render, redirect, get_object_or_404
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from android.models import AndroidPost

from django.db.models import Q

BLOG_POSTS_PER_PAGE = 9

def android_screen_view(request, *args, **kwargs):
	
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	


	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "android/home.html", context)




def detail_blog_view(request, slug):

	context = {}
	blog_posts_list = sorted(AndroidPost.objects.all(), key=attrgetter('date_updated'), reverse=False)
	blog_post = get_object_or_404(AndroidPost, slug=slug)
	context['blog_post'] = blog_post
	context['blog_posts_list'] = blog_posts_list

	return render(request, 'android/detail_blog.html', context)



def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = AndroidPost.objects.filter(
			Q(title__contains=q)|
			Q(body__icontains=q)
			).distinct()
		for post in posts:
			queryset.append(post)

	# create unique set and then convert to list
	return list(set(queryset)) 


