from django.urls import path
from donations import views

urlpatterns = [
    path('', views.api_donations_list, name='api_donations_list'),
    path('<int:id>/', views.api_get_donation_by_id, name='api_get_donation_by_id'),
    path('create', views.api_create_donation, name='api_create_donation'),
    path('<int:id>/update', views.api_update_donation, name='api_update_donation'),
    path('<int:id>/delete', views.api_delete_donation, name='api_delete_donation'),
]