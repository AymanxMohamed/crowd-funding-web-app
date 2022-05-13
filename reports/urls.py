from django.urls import path
from reports import views


urlpatterns = [
    path('', views.api_reports_list, name='report_list'),
    path('create/', views.api_create_report, name='create_report'),
    path('<int:pk>/', views.api_get_report_by_id, name='get_report_by_id'),
    path('<int:pk>/delete/', views.api_delete_report, name='delete_report'),
]

