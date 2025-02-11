from django.urls import path
from .views import UserLoginView, UserLogoutView
from .views import staff_only_view

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(next_page='/'), name='logout'),
    path('staff/', staff_only_view, name='staff'),
]