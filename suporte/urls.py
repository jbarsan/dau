from django.urls import include, path
from suporte import views as suporte_views

urlpatterns = [
    path('entrada/', suporte_views.entradas, name='entradas'),
    path('entrada/<int:pk>/', suporte_views.list_entradas, name='list_entradas'),
    #path('entrada/<int:pk>/novo_atendimento', suporte_views.novo_atendimento, name='novo_atendimento'),
    path('equipamento/', suporte_views.equipamentos, name='equipamentos'),
    path('equipamento/<int:pk>/', suporte_views.list_equipamentos, name='list_equipamentos'),
    #path('equipamento/<int:pk>/novo/', suporte_views.novo_equipamento, name='novo_equipamento'),
    path('departamento/', suporte_views.departamentos, name='departamentos'),
    path('departamento/<int:pk>/', suporte_views.list_departamentos, name='list_departamentos'),

]
