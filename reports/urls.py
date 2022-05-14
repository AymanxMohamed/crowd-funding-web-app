from django.urls import path
from reports import views

urlpatterns = [
    path('comments', views.api_comment_reports, name='comment_reports'),
    path('comments/<int:pk>/', views.api_get_comment_report_by_id, name='get_comment_report_by_id'),
    path('comments/create/', views.api_create_comment_report, name='create_comment_report'),
    path('comments/<int:pk>/', views.api_delete_comment_report, name='delete_comment_report'),

    path('projects', views.api_project_reports, name='project_reports'),
    path('projects/<int:pk>/', views.api_get_project_report_by_id, name='get_project_report_by_id'),
    path('projects/create/', views.api_create_project_report, name='create_project_report'),
    path('projects/<int:pk>', views.api_delete_project_report, name='delete_project_report'),
]


