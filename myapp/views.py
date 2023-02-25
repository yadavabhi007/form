from django.shortcuts import render, HttpResponseRedirect
from .models import User
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import JsonResponse

# Create your views here.

class FormData(TemplateView):
    template_name = 'myapp/home.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        data = User.objects.all()
        context = {'data':data}
        return context
    def post(self, request):
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        city=request.POST['city']
        fm = User(name=name, email=email, mobile=mobile, city=city)
        if request.is_ajax():
            fm.save()
            response = {'msg':'Your form has been submitted successfully'}
            return JsonResponse(response)
        return HttpResponseRedirect("/")


class AllData(ListView):
    model = User
    template_name = 'myapp/show.html'
    context_object_name = 'data'
    data = User.objects.all()
    context = {'data':data}
