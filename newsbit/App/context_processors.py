from .models import Category, Post
from django.shortcuts import render
from django.db.models.functions import Random
from django.db.models import Q







def categories(request):
    return {'categories': Category.objects.all()}

def viewz(request):
    categories = Category.objects.all()[:4]
    category_posts = {}
    for category in categories:
        posts = category.post_set.all()
        if posts:
            post = posts.first()
            category_posts[category] = post
    return  {'category_posts': category_posts}


def category_posts(request):
    categories = Category.objects.all()
    allthings= {'categories': categories}
    return allthings

def post_info(request):
    post_id = request.GET.get('post_id')
    if post_id:
        try:
            post = Post.objects.get(id=post_id)
            return {'post': post}
        except Post.DoesNotExist:
            pass
    return {}


def get_random_post(request):
    random_post = Post.objects.filter(id__gte=1).annotate(random_number=Random()).order_by('random_number').first()

    if random_post:
        # Get the associated category of the random post
        random_category = random_post.categories.first()
    else:
        random_category = None

    return {'random_post': random_post, 'random_category': random_category}

def get_random_posts(request):
    random_posts = Post.objects.filter(id__gte=1).annotate(random_number=Random()).order_by('random_number')[:4]

    # Get the associated categories for each random post
    random_categories = [post.categories.first() if post else None for post in random_posts]

    return {'random_posts': random_posts, 'random_categories': random_categories}

# context_processors.py





def search(request):
    categories = Category.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        categories = categories.filter(name__icontains=search_query)
        for category in categories:
            category.posts = category.post_set.filter(title__icontains=search_query)
    return {'categories': categories, 'search_query': search_query}
