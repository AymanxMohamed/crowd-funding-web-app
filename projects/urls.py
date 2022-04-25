from django.urls import path
from projects import views

urlpatterns = [
    path('', views.api_projects_list, name='project_list'),
    path('<int:id>/', views.api_get_project_by_id, name='project_detail'),
    path('create/', views.api_create_project, name='project_create'),
    path('<int:id>/update/', views.api_update_project, name='project_update'),
    path('<int:id>/delete/', views.api_delete_project, name='project_delete'),
]