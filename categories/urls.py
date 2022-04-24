from django.urls import path
from categories import views
urlpatterns = [
    path('', views.CategoryList.as_view()),
    path('<int:pk>/', views.CategoryDetail.as_view()),
]