from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('update', views.update_user, name='update_user'),
    path('remove', views.delete_user, name='delete_user'),
    path('<user_id>/projects', views.user_projects, name='user_projects'),
]
