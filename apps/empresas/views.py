from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse

from .models import Empresa

class EmpresaCreate(CreateView):
  model = Empresa
  fields = ['nome',]

  def form_valid(self, form):
    obj = form.save()

    # Atribuindo empresa criada ao funcionário logado
    funcionario = self.request.user.funcionario
    funcionario.empresa = obj
    funcionario.save()

    return HttpResponse('OK')

class EmpresaEdit(UpdateView):
  model = Empresa
  fields = ['nome',]