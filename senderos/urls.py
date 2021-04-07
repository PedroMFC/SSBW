from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('añadir', views.añadir, name='añadir'),
    path('info/<str:id>/', views.info, name='info'),
    path('editar/<str:id>/', views.editar, name='editar'),
    path('borrar/<str:id>/', views.borrar, name='borrar'),
]