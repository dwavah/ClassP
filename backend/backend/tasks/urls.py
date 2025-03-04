from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),  # Handles GET (list) & POST (create)
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # Handles GET (retrieve), PUT (update), DELETE (remove)
]
