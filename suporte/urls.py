from django.urls import include, path
from suporte import views as suporte_views

urlpatterns = [
    path('entrada/<int:pk>/', suporte_views.entradas, name='entradas'),

]
