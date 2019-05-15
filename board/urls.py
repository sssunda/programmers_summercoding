from django.urls import path
from . import views

app_name ='board'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<id>/detail/', views.post_detail, name='post_detail'),
    path('new/', views.post_add, name='post_add'),
    path('<id>/delete/', views.post_delete, name='post_delete'),
    path('<pk>/edit/', views.post_edit, name='post_edit'),
    path('<id>/complete/<url>', views.complete, name ='complete'),
    
]
