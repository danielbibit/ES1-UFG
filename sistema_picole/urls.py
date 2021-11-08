"""sistema_picole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sistema_picole.sistema_venda import views as sistema_venda_views
from sistema_picole.landing_page import views as landing_page_views
from sistema_picole.sistema_venda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema/estoque/edit/<int:id>', views.edit_estoque),
    path('sistema/vendas/edit/<int:id>', views.edit_venda),
    path('sistema/vendas/adiciona_venda/', views.adiciona_venda),
    path('sistema/estoque/adiciona_picole/', views.adiciona_picole),
    path('sistema/estoque/adiciona_lote/', views.adiciona_lote),
    path('sistema/vendas/', views.venda),
    path('sistema/estoque/', views.estoque),
    path('sistema/', sistema_venda_views.index),
    path('', landing_page_views.index)

]
