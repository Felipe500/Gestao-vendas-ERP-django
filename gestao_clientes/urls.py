from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path, include
from clientes import urls as clientes_urls
from produtos import urls as produtos_urls
from vendas import urls as vendas_urls
from home import urls as home_urls
from movimentacoes import urls as movi_urls
from configuracoes import urls as settings_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(home_urls)),
    path('', include(settings_urls)),
    path('', include(movi_urls)),
    path('clientes/', include(clientes_urls)),
    path('produtos/', include(produtos_urls)),
    path('vendas/', include(vendas_urls)),
    path('', include('autenticacao.urls'), name='login2'),

    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

AdminSite.site_header  =  "Gestão de Vendas"
AdminSite.site_title  =  "Seja bem-vindo"
AdminSite.index_title  =  "Administração"
