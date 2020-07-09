from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('introduce/', views.introduce, name = "introduce"),
    path('propile/<int:designer_id>/', views.detail, name = "detail"),
    path('new/', views.new, name="new"),
    path('creat/',views.creat, name="creat"),
    path('delete/<int:designer_id>/', views.delete, name = "delete"),
] 