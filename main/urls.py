"""art URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
    path('', views.index, name='index'),
    path('add-exhibit',views.AddExhibitView.as_view(),name='add-exhibit'),
    path('list-exhibit',views.ListExhibitView.as_view(),name='list-exhibit'),
    path('delete-exhibit/<int:pk>',views.DeleteExhibitView.as_view(),name='delete-exhibit'),
    path('update-exhibit/<int:pk>',views.UpdateExhibitView.as_view(),name='update-exhibit'),
    path('api/<int:pk>',views.APIView.as_view(),name='api'),
    path('api',views.APIView.as_view(),name='api'),


]
