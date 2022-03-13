from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from django.urls import path, include

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login')
]