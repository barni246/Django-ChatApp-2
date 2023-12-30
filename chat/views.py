from django.shortcuts import render
from .models import Message, Chat

# Create your views here.
def index(request):
    if request.method == 'POST':
      #  print('Recieved data: ' + request.POST['textmessage']) Junus Version
        text_message = request.POST.get('textmessage', '')
        print('Recieved data: ' + text_message)
        Message.objects.create(text = request.POST.get('textmessage', '' ), chat = None, author = request.user, receiver = request.user)
    return render(request, 'chat/index.html', {'username': ' Barnabas'})
