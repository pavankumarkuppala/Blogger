from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create_blog/', views.create_blog, name="create_blog"),
    path('<int:blog_id>/blog_detail/', views.blog_detail, name="blog_detail"),
    path('<int:blog_id>/edit_blog/', views.edit_blog, name="edit_blog"),
    path('<int:blog_id>/delete_blog/', views.delete_blog, name="delete_blog"),
    path('register/', views.register, name="register"),
    path('my_blogs/', views.my_blogs, name="my_blogs"),
    path('search_blog/', views.search_blog, name='search_blog'),
]