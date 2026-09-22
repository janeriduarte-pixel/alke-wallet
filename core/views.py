from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cuenta, Cliente

class CuentaListView(LoginRequiredMixin, ListView):
    model = Cuenta
    template_name = 'core/cuenta_list.html'
    context_object_name = 'cuentas'

class CuentaDetailView(LoginRequiredMixin, DetailView):
    model = Cuenta
    template_name = 'core/cuenta_detail.html'

class CuentaCreateView(LoginRequiredMixin, CreateView):
    model = Cuenta
    fields = ['cliente', 'tipo', 'saldo']
    template_name = 'core/cuenta_form.html'
    success_url = reverse_lazy('cuenta-list')

class CuentaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cuenta
    fields = ['tipo', 'saldo']
    template_name = 'core/cuenta_form.html'
    success_url = reverse_lazy('cuenta-list')

class CuentaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cuenta
    template_name = 'core/cuenta_confirm_delete.html'
    success_url = reverse_lazy('cuenta-list')

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