from allauth.account import app_settings
from allauth.account.utils import get_next_redirect_url, complete_signup, passthrough_next_redirect_url
from allauth.account.views import RedirectAuthenticatedUserMixin, CloseableSignupMixin, AjaxCapableProcessFormViewMixin, \
    sensitive_post_parameters_m
from allauth.exceptions import ImmediateHttpResponse
from allauth.utils import get_form_class, get_request_param
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View
from allauth.account.forms import BaseSignupForm,SignupForm
from produtos.models import Categoria, Produto


def home(request):
    #    import pdb; pdb.set_trace()
    value1 = 10
    value2 = 20
    res =value2
    return render(request, 'home/home.html', {'result': res})


def my_logout(request):
    logout(request)
    1 + 1
    return redirect('home')


class HomePageView(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Ola, seja bem vindo ao curso de Django advanced'
        return context


class MyView(View):

    def get(self, request, *args, **kwargs):
        HttpResponse.set_cookie('color', 'blue', max_age=1000)
        mycookie = request.COOKIES.get('color')
        print(mycookie)
        return HttpResponse

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')



class SignupView(

    CloseableSignupMixin,
    AjaxCapableProcessFormViewMixin,
    FormView,
):
    template_name = 'home/register.html'
    form_class = SignupForm
    redirect_field_name = "next"
    success_url = None



    def get_form_class(self):
        return get_form_class(app_settings.FORMS, "signup", self.form_class)

    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (
            get_next_redirect_url(self.request, self.redirect_field_name)
            or self.success_url
        )
        return ret

    def form_valid(self, form):
        # By assigning the User to a property on the view, we allow subclasses
        # of SignupView to access the newly created User instance
        self.user = form.save(self.request)
        try:
            return complete_signup(
                self.request,
                self.user,
                app_settings.EMAIL_VERIFICATION,
                self.get_success_url(),
            )
        except ImmediateHttpResponse as e:
            return e.response



signup = SignupView.as_view()

def filtra_produtos(request):
    id_categoria = request.GET['categoria_id']
    print( request.GET['categoria_id'] ,'ddd')

    categoria = Categoria.objects.get(id=id_categoria)

    qs_json = serializers.serialize('json', categoria.produto_set.all())
    return HttpResponse(qs_json, content_type='application/json')