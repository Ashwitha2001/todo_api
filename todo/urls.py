from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('todos/', views.get_todos, name='get_todos'),  
    path('todos/create/', views.create_todo, name='create_todo'),  
    path('todos/<int:todo_id>/update/', views.update_todo, name='update_todo'),  
    path('todos/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'), 
]
