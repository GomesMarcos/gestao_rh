from django.contrib.auth.models import User
from django.views.generic import (
  ListView,
  UpdateView,
  DeleteView,
  CreateView
)
from django.urls import reverse_lazy

from .models import RegistroHoraExtra


class HoraExtraList(ListView):
  model = RegistroHoraExtra

  def get_queryset(self):
    empresa_logada = self.request.user.funcionario.empresa
    return self.model.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
  model = RegistroHoraExtra
  fields = ['motivo', 'funcionario', 'horas']

class HoraExtraDelete(DeleteView):
  model = RegistroHoraExtra
  success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
  model = RegistroHoraExtra
  fields = ['motivo', 'funcionario', 'horas']

  class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtra