from django.urls import path 
from . import views
from App.views import CategoryPostsView

urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('category/<int:pk>/', CategoryPostsView.as_view(), name='category_posts'),
    path('', views.design, name='design'),
    path('', views.navigation, name='navigation'),
    path('', views.random_post, name='random_post'),
    path('', views.random_posts, name='random_posts'),
    path('search/', views.search, name='category_search'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.footer, name='footer'),
    path('post/<int:post_id>/', views.post_view, name='post_view')

    

    
    
    

   
    
    
   
   
]