from django.urls import path
from .views import Settings, Settings2,Maq_cartaoList,Maq_cartaoCreate,Maq_cartaoUpdate
from django.views.generic.base import TemplateView

urlpatterns = [
    path('settings2', Settings, name="settings_app2"),
    path('settings', Maq_cartaoList.as_view(), name="settings_app"),
    path('create_new_maq', Maq_cartaoCreate.as_view(), name="create_new_maq"),
    path('update_maq/<int:id>/', Maq_cartaoUpdate.as_view(), name="update_maquina")
]