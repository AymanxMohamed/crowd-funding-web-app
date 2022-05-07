from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenRefreshView)
from users.views import MyTokenObtainPairView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('categories/', include('categories.urls')),
    path('comments/', include('comments.urls')),
    path('donations/', include('donations.urls')),
    path('projects/', include('projects.urls')),
    path('tags/', include('tags.urls')),
    path('users/', include('users.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]
