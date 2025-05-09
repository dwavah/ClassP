from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),  # GET (all), POST
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # GET (by id), PUT, DELETE
]
