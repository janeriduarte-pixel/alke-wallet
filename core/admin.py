from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion, Etiqueta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipo', 'saldo', 'fecha_creacion')
    list_filter = ('tipo',)
    search_fields = ('cliente__nombre',)

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('cuenta', 'tipo', 'monto', 'fecha')
    list_filter = ('tipo',)

admin.site.register(Etiqueta)