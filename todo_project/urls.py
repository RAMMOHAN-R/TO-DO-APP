# todo/urls.py
from django.urls import path
from todo import views

urlpatterns = [
    path('',views.login, name='login'),
    path('tasks/<int:user_id>/', views.task_list, name='task_list'),
    path('delete_task/<int:task_id>/<int:user_id>/', views.delete_task, name='delete_task'),
]
