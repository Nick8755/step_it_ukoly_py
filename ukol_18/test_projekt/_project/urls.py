from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

    path('age/', views.age),

    path('admin/', admin.site.urls),
]
