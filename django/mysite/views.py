# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request: HttpRequest) -> HttpResponse:
    print(request.user)
    return render(request, 'index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

