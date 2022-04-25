from django.urls import path
from projects import views

urlpatterns = [
    path('', views.api_projects_list, name='project_list'),
    path('<int:id>/', views.api_get_project_by_id, name='project_detail'),
]