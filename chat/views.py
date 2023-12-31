from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
      #  print('Recieved data: ' + request.POST['textmessage']) Junus Version
        text_message = request.POST.get('textmessage', '')
        print('Recieved data: ' + text_message)
        myChat = Chat.objects.get(id = 1)
        Message.objects.create(text = request.POST.get('textmessage', '' ), chat = myChat, author = request.user, receiver = request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})


def login_view(request):
  redirect = request.GET.get('next')
  if request.method == 'POST':
    user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
    if user:
      login(request, user)
      return HttpResponseRedirect(request.POST.get('redirect'))
    else:
      return render(request, 'auth/login.html', {'wrongPassword':True , 'redirect': redirect})
  return render(request, 'auth/login.html', {'redirect': redirect})


def register_view(request):
    return render(request, 'auth/register.html')

