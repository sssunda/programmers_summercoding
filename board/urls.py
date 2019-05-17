from django.urls import path
from . import views

app_name ='board'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('rank_update/', views.update_post_list_rank, name="update_post_list_rank"),
    path('<id>/detail/', views.post_detail, name='post_detail'),
    path('new/', views.add_post, name='add_post'),
    path('<id>/delete/', views.delete_post, name='delete_post'),
    path('<pk>/edit/', views.edit_post, name='edit_post'),
    path('<id>/complete/<url>', views.complete, name ='complete'),
    
]
