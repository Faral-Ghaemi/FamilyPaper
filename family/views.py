from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic
from django.views.generic.list import ListView
from . import models
from django.template import loader
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta
from django.contrib.auth import authenticate, login, logout
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    children = models.Childrens.objects.get(user=request.user)
    family = models.Childrens.objects.filter(family=children.family)
    messages = ""
    if request.method == "POST":
        try:
            card_number = request.POST.get('card_number')
            children2 = models.Childrens.objects.get(card_number=card_number)
            score =  request.POST.get('score')
            score = int(score)
            if children.score >= score:
                children.score -= score
                children.save()
                children2.score += score
                children2.save()
                messages = "با موفقیت انجام شد"
            else:
                messages = "شما امتیاز کافی را ندارید"
        except models.Childrens.DoesNotExist:
            messages = "چنین شماره کارتی وجود ندارد"

    context = {
        'family': family,
        'children': children,
        'messages' : messages,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context,request))

@csrf_exempt
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('login.html')
