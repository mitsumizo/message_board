from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<str:target_name>/', views.post_person, name='post_person'),
    path('error/', views.error_page, name='error_page')
]
