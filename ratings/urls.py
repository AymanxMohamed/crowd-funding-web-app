from django.urls import URLPattern, path
from ratings import views


urlpatterns = [
    path('', views.api_ratings_list, name='rating_list'),
    path('create/', views.api_create_rating, name='create_rating'),
    path('<int:pk>/', views.api_get_rating_by_id, name='get_rating_by_id'),
    path('<int:pk>/update/', views.api_update_rating, name='update_rating'),
    path('<int:pk>/delete/', views.api_delete_rating, name='delete_rating'),
]