from django.shortcuts import render
from .models import Post,Category
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
import random
from django.views.generic import ListView
from django.views.generic import TemplateView
from .context_processors import get_random_post, get_random_posts
from django.urls import reverse

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

class CategoryPostsView(ListView):
    model = Post
    template_name = 'category_posts.html'
    paginate_by = 5  # Number of items to display per page

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(categories__pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], self.paginate_by)
        page = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page)
        return context
    
    

def design(request):
    return render(request, 'design.html')




def navigation(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    template = 'navigation.html'
    return render(request, template, context)

    

def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')

def footer(request):
    return render(request, 'footer.html')

def contact(request):
    return render(request, 'contact.html')


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post_view.html', context)

class HotNewsView(TemplateView):
    template_name = "hotnews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get a random category and its related posts
        categories = Category.objects.all()
        random_category = random.choice(categories)
        related_posts = Post.objects.filter(category=random_category)[:1]

        # Add the category and related posts to the context
        context["random_category"] = random_category
        context["related_posts"] = related_posts

        return context

def random_post(request):
    random_post = get_random_post()
    context = {'post': random_post}
    return render(request, 'random.html', context)

def random_posts(request):
    random_post = get_random_posts()
    context = {'post': random_post}
    return render(request, 'related.html', context)


def search(request):
    categories = Category.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        categories = categories.filter(name__icontains=search_query)
    context = {'categories': categories, 'search_query': search_query}
    return render(request, 'search.html', context)