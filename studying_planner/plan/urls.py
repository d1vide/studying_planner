from django.urls import path

from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('plans/<int:pk>/edit/', views.plan_create, name='edit'),
    path('plans/<int:pk>/delete/', views.plan_delete, name='delete'),
    path('plans/<int:pk>/', views.plan_detail, name='detail'),
    path('plans/', views.plan_list, name='list'),
    path('tasks/', views.task_list, name='tasklist'),
    path('plans/create/', views.plan_create, name='create'),
    path('button_do_task/<int:pk>/', views.do_task, name='button_do_task'),
]
