from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    # Uno a Uno: cada Cliente extiende a un User de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    TIPO_CHOICES = [('AHORRO', 'Ahorro'), ('CORRIENTE', 'Corriente')]

    # Muchos a Uno: un cliente puede tener varias cuentas
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cuentas')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='AHORRO')
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cuenta {self.tipo} de {self.cliente.nombre}'


class Transaccion(models.Model):
    TIPO_MOV = [('DEPOSITO', 'Depósito'), ('RETIRO', 'Retiro'), ('TRANSFERENCIA', 'Transferencia')]

    # Muchos a Uno: una cuenta tiene muchas transacciones
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=15, choices=TIPO_MOV)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    # Muchos a Muchos: etiquetas o categorías asociadas a una transacción
    etiquetas = models.ManyToManyField('Etiqueta', blank=True, related_name='transacciones')

    def __str__(self):
        return f'{self.tipo} - {self.monto}'


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre