from django.urls import path
from comments import views

urlpatterns = [
    path('', views.api_comments_list, name='comments_list'),
    path('<int:id>/', views.api_get_comment_by_id, name='get_comment_by_id'),
    path('create', views.api_create_comment, name='create_comment'),
    path('<int:id>/update', views.api_update_comment, name='update_comment'),
    path('<int:id>/delete', views.api_delete_comment, name='delete_comment'),
]