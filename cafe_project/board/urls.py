"""cafe_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.board_read, name="board_read"),
    path('read/<int:pk>', views.board_read_one, name='board_read_one'),
    path('create/', views.board_create, name='board_create'),
    path('update/<int:pk>', views.board_update, name='board_update'),
    path('delete/<int:pk>', views.board_delete, name='board_delete'),
]
