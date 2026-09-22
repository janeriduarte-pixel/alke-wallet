from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cuenta, Cliente
 
 
class CuentaListView(LoginRequiredMixin, ListView):
    model = Cuenta
    template_name = 'core/cuenta_list.html'
    context_object_name = 'cuentas'
 
    def get_queryset(self):
        # Solo las cuentas del cliente asociado al usuario logueado
        return Cuenta.objects.filter(cliente__usuario=self.request.user)
 
 
class CuentaDetailView(LoginRequiredMixin, DetailView):
    model = Cuenta
    template_name = 'core/cuenta_detail.html'
 
    def get_queryset(self):
        return Cuenta.objects.filter(cliente__usuario=self.request.user)
 
 
class CuentaCreateView(LoginRequiredMixin, CreateView):
    model = Cuenta
    fields = ['tipo', 'saldo']  # 'cliente' ya no se elige manualmente
    template_name = 'core/cuenta_form.html'
    success_url = reverse_lazy('cuenta-list')
 
    def form_valid(self, form):
        # Asigna automáticamente la cuenta al cliente del usuario logueado
        cliente = get_object_or_404(Cliente, usuario=self.request.user)
        form.instance.cliente = cliente
        return super().form_valid(form)
 
 
class CuentaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cuenta
    fields = ['tipo', 'saldo']
    template_name = 'core/cuenta_form.html'
    success_url = reverse_lazy('cuenta-list')
 
    def get_queryset(self):
        return Cuenta.objects.filter(cliente__usuario=self.request.user)
 
 
class CuentaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cuenta
    template_name = 'core/cuenta_confirm_delete.html'
    success_url = reverse_lazy('cuenta-list')
 
    def get_queryset(self):
        return Cuenta.objects.filter(cliente__usuario=self.request.user)
 
 
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cliente.objects.create(usuario=user, nombre=user.username, email=f"{user.username}@example.com")
            login(request, user)
            return redirect('cuenta-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})