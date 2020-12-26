from django.contrib.auth.models import User
from django.views.generic import (
  ListView,
  UpdateView,
  DeleteView,
  CreateView
)
from django.urls import reverse_lazy

from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
  model = RegistroHoraExtra

  def get_queryset(self):
    empresa_logada = self.request.user.funcionario.empresa
    return self.model.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
  model = RegistroHoraExtra
  form_class = RegistroHoraExtraForm

  def get_form_kwargs(self):
    kwargs = super(HoraExtraEdit, self).get_form_kwargs()
    kwargs.update({'user': self.request.user})
    return kwargs

class HoraExtraDelete(DeleteView):
  model = RegistroHoraExtra
  success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):

  model = RegistroHoraExtra
  form_class = RegistroHoraExtraForm

  def get_form_kwargs(self):
    kwargs = super(HoraExtraCreate, self).get_form_kwargs()
    kwargs.update({'user': self.request.user})
    return kwargs
