from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('añadir', views.añadir, name='añadir'),
    path('info/<str:id>/', views.info, name='info'),
    path('editar/<str:id>/', views.editar, name='editar'),
    path('borrar/<str:id>/', views.borrar, name='borrar'),
    path('api/excursiones', views.ExcursionesView.as_view(), name="excursiones"),
    path('api/excursion/<str:id>', views.ExcursiónView.as_view(), name="excursión"),
    path('cambiarlikes/<str:id>', views.cambiarlikes, name="cambiarlikes"),
]