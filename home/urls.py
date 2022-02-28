from django.urls import path
from .views import home, my_logout
from .views import home, my_logout, HomePageView, MyView,SignupView, filtra_produtos
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
    path('home2/', TemplateView.as_view(template_name='home2.html')),
    path('home3/', HomePageView.as_view(template_name='home3.html')),
    path('view/', MyView.as_view()),
    path('register/', SignupView.as_view(),name="register"),
    path('filtra_produtos/', filtra_produtos,name="filtra_produtos"),
]
