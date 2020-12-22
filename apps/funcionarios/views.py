from django.contrib.auth.models import User
from django.views.generic import (
  ListView,
  UpdateView,
  DeleteView,
  CreateView
)
from django.urls import reverse_lazy

from .models import Funcionario

class FuncionariosList(ListView):
  model = Funcionario

  def get_queryset(self):
    empresa_logada = self.request.user.funcionario.empresa
    return self.model.objects.filter(empresa=empresa_logada)

class FuncionariosEdit(UpdateView):
  model = Funcionario
  fields = ['nome', 'departamentos']

class FuncionariosDelete(DeleteView):
  model = Funcionario
  success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreate(CreateView):
  model = Funcionario
  fields = ['nome', 'departamentos']

  def form_valid(self, form):
    # Salvando funcionário temporariamente em memória
    funcionario = form.save(commit=False)

    """
    Coletando campos faltantes do model
    contidos na sessão
    """
    username = funcionario.nome.split(' ')[0] + ' ' + funcionario.nome.split(' ')[1]
    funcionario.empresa = self.request.user.funcionario.empresa
    funcionario.user = User.objects.create(username=username)
    # armazenando funcionário no banco
    funcionario.save()
    
    return super(FuncionarioCreate, self).form_valid(form)