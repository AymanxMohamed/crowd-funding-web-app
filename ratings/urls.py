from django.urls import URLPattern, path
from ratings import views


urlpatterns = [
    path('', views.api_ratings_list, name='rating_list'),
]