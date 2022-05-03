from django.urls import path
from tags import views

urlpatterns = [
    path('', views.api_tags_list, name='api_tags_list'),
    path('<int:id>/', views.api_get_tag_by_id, name='api_get_tag_by_id'),
    path('create', views.api_create_tag, name='api_create_tag'),
    path('<int:id>/update', views.api_update_tag, name='api_update_tag'),
    path('<int:id>/delete', views.api_delete_tag, name='api_delete_tag'),
]