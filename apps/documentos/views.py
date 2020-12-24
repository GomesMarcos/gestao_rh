from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from .models import Documento

class DocumentoCreate(CreateView):
  model = Documento
  fields = ['titulo', 'arquivo']

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    form.instance.pertence_id = self.kwargs['funcionario_id']

    if form.is_valid():
      return self.form_valid(form)

    return self.form_invalid(form)

class DocumentoEdit(UpdateView):
  model = Documento
  fields = ['nome',]