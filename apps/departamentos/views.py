from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Departamento


class DepartamentosList(ListView):
  model = Departamento

  def get_queryset(self):
      empresa_logada = self.request.user.funcionario.empresa
      return Departamento.objects.filter(empresa=empresa_logada)
  

class DepartamentosEdit(UpdateView):
  model = Departamento
  fields = ['nome']

class DepartamentosDelete(DeleteView):
  model = Departamento
  success_url = reverse_lazy('list_departamentos')

class DepartamentoCreate(CreateView):
  model = Departamento
  fields = ['nome']

  
  def form_valid(self, form):
    # Salvando funcionário temporariamente em memória
    departamento = form.save(commit=False)

    """
    Coletando campos faltantes do model
    contidos na sessão
    """
    departamento.empresa = self.request.user.funcionario.empresa
    # armazenando funcionário no banco
    departamento.save()
    
    return super(DepartamentoCreate, self).form_valid(form)