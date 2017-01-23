from django.shortcuts import render
from .models import Map
from .forms import MapForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    maps = Map.objects.all()
    form = MapForm()
    return render(request, 'index.html', {'maps':maps, 'form':form})

def mapview(request, id):
    map = Map.objects.get(pk=id)
    return render(request, 'map_view.html', {'map':map})


def post_map(request):
    form = MapForm(request.POST)
    if form.is_valid():
        map = Map(name = form.cleaned_data['name'],
                  longitude_val = form.cleaned_data['center_longitude_val'],
                  latitude_val = form.cleaned_data['center_latitude_val'],
                  left_longitude_val = form.cleaned_data['left_longitude_val'],
                  left_latitude_val = form.cleaned_data['left_latitude_val'],
                  right_longitude_val = form.cleaned_data['right_longitude_val'],
                  right_latitude_val = form.cleaned_data['right_latitude_val'])
        map = form.save(commit = False)
        map.user = request.user
        map.save()
        return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    maps = Map.objects.filter(user=user)
    return render(request, 'profile.html',
                  {'username':username,
                   'maps':maps})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print("User is not active")
            else:
                print("Incorrect username and password combination")                
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
                  
                  
                  
                  
