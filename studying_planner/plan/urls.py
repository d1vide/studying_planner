from django.urls import path

from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('plans/<int:pk>/edit/', views.plan_create, name='edit'),
    path('plans/<int:pk>/delete/', views.plan_delete, name='delete'),
    path('plans/<int:pk>/', views.plan_detail, name='detail'),
    path('plans/', views.plan_list, name='list'),
    path('plans/create/', views.plan_create, name='create')
]
