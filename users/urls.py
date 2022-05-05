from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('<int:user_id>/update',views.update_user, name='update_user'),
]
