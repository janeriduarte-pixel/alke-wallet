from django.urls import path
from . import views

urlpatterns = [
    path('cuentas/', views.CuentaListView.as_view(), name='cuenta-list'),
    path('cuentas/<int:pk>/', views.CuentaDetailView.as_view(), name='cuenta-detail'),
    path('accounts/registro/', views.registro, name='registro'),
    path('cuentas/nueva/', views.CuentaCreateView.as_view(), name='cuenta-create'),
    path('cuentas/<int:pk>/editar/', views.CuentaUpdateView.as_view(), name='cuenta-update'),
    path('cuentas/<int:pk>/eliminar/', views.CuentaDeleteView.as_view(), name='cuenta-delete'),
]