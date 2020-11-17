from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from visitor.models import Media
from .forms import MediaForm, MediaUpdateForm

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('approval')
    else:    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('approval')
            else:
                messages.info(request, 'Nome ou senha incorreto.')

        return render(request, 'visitor/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def approval(request):
    medias = Media.objects.all()

    return render(request, 'visitor/approval.html', {'medias':medias})

def gallery(request):
    mediasAllowed = Media.objects.filter(allowed=True)

    return render(request, 'visitor/gallery.html', {'mediasAllowed':mediasAllowed})

def uploadPhoto(request):
    mediaForm = MediaForm()

    if request.method == 'POST':
        mediaForm = MediaForm(request.POST, request.FILES)
        if mediaForm.is_valid():
            mediaForm.save()
            return redirect('/')

    return render(request, 'visitor/dashboard.html', {'mediaForm':mediaForm})

@login_required(login_url='login')
def updatePhotoState(request, pk):

    media = Media.objects.get(id=pk)
    mediaForm = MediaUpdateForm(instance=media)

    if request.method == 'POST':
        mediaForm = MediaUpdateForm(request.POST, instance=media)
        if mediaForm.is_valid():
            mediaForm.save()
            return redirect('/approval')

    return render(request, 'visitor/dashboard.html', {'mediaForm':mediaForm})