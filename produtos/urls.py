from django.urls import path, include
from .views import *


urlpatterns = [
    #path ('Caminho/da/url',
    #ClasseLÁdoView.as_view(),
    #name="nomeDessaURL")
    

    path('inicio/',PaginaInicialView.as_view(), name="index"),
]
