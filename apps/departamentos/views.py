from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Departamento


class DepartamentosList(ListView):
  model = Departamento

  def get_queryset(self):
      empresa_logada = self.request.user.funcionario.empresa
      return Departamento.objects.filter(empresa=empresa_logada)
  

class DepartamentosEdit(UpdateView):
  pass

class DepartamentosDelete(DeleteView):
  pass

class DepartamentoCreate(CreateView):
  model = Departamento
  fields = ['nome', 'empresa']
