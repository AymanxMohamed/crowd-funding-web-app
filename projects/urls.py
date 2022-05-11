from django.urls import path
from projects import views

urlpatterns = [
    path('', views.api_all_projects, name='project_list'),
    path('myprojects', views.api_my_projects, name='my_project_list'),
    path('featured', views.api_featured_projects, name='featured_project_list'),
    path('latest', views.api_latest_projects, name='latest_project_list'),
    path('<int:id>/', views.api_get_project_by_id, name='project_detail'),
    path('create/', views.api_create_project, name='project_create'),
    path('<int:id>/update/', views.api_update_project, name='project_update'),
    path('<int:id>/delete/', views.api_delete_project, name='project_delete'),
    path('<int:id>/images/', views.project_images, name='project_images'),
    path('search/<str:query>', views.api_search_projects, name='project_search'),
]