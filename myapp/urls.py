from django.urls import path
from . import views
#Here every url is associated with a view. 
urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
]
