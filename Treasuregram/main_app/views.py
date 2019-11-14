from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Treasure
from .forms import TreasureForm

def homepage_view(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request,'homepage_view.html', {'treasures':treasures, 'form':form})


def details_view(request, treasure_id):
    treasure = Treasure.objects.get(id = treasure_id)
    return render(request,'details_view.html',{'treasure':treasure})

def post_treasure_view(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = form.save(commit = False)
        treasure.user = request.user
        treasure.save()
    
    return HttpResponseRedirect('/')

def user_profile_view(request,user_name):
    user = User.objects.get(username = user_name)
    treasures = Treasure.objects.filter(user = user)
    return render(request, 'profile_view.html', {'username': user , 'treasures': treasures})
