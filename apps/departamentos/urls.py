from django.urls import path
from .views import (
    DepartamentosList,
    DepartamentosEdit,
    DepartamentosDelete,
    DepartamentoCreate,
)

urlpatterns = [
    path('', DepartamentosList.as_view(), name="list_departamentos"),
    path('editar/<int:pk>', DepartamentosEdit.as_view(), name="update_departamento"),
    path('deletar/<int:pk>', DepartamentosDelete.as_view(), name="delete_departamento"),
    path('novo/', DepartamentoCreate.as_view(), name="create_departamento"),
]
