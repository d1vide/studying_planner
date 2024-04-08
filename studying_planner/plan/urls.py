from django.urls import path

from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('plans/<int:pk>/', views.plan_detail, name='plandetail'),
    path('plans/', views.plan_list, name='planlist'),
    
]
