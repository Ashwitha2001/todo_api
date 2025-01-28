from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at', 'updated_at', 'user')
    list_filter = ('completed', 'user')  
    search_fields = ('title', 'description') 
    ordering = ('-created_at',) 
    list_editable = ('completed',) 

admin.site.register(Todo, TodoAdmin)


