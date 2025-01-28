from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Todo

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email', '')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return JsonResponse({"message": "User created successfully!"}, status=201)
    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful!"}, status=200)
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=400)
        

@csrf_exempt
@login_required
def create_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description', '')
        todo = Todo.objects.create(title=title, description=description, user=request.user)
        return JsonResponse({'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed}, status=201)


@login_required
def get_todos(request):
    if request.method == 'GET':
        todos = Todo.objects.filter(user=request.user)
        todos_data = [{'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed} for todo in todos]
        return JsonResponse(todos_data, safe=False)


@csrf_exempt
@login_required
def update_todo(request, todo_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            todo = Todo.objects.get(id=todo_id, user=request.user)
            todo.title = data.get('title', todo.title)
            todo.description = data.get('description', todo.description)
            todo.completed = data.get('completed', todo.completed)
            todo.save()
            return JsonResponse({'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed})
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)


@csrf_exempt
@login_required
def delete_todo(request, todo_id):
    if request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=todo_id, user=request.user)
            todo.delete()
            return JsonResponse({'message': 'Todo deleted successfully'}, status=204)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)
