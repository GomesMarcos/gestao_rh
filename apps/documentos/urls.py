from django.urls import path
from .views import DocumentoCreate, DocumentoEdit

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
    # path('deletar/<int:pk>', DocumentoEdit.as_view(), name='delete_documento'),
]
