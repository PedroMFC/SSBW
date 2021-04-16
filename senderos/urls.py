from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # new
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('añadir', views.añadir, name='añadir'),
    path('info/<str:id>/', views.info, name='info'),
    path('editar/<str:id>/', views.editar, name='editar'),
    path('borrar/<str:id>/', views.borrar, name='borrar'),
]