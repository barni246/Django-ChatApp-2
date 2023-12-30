from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
      #  print('Recieved data: ' + request.POST['textmessage']) Junus Version
        text_message = request.POST.get('textmessage', '')
        print('Recieved data: ' + text_message)
    return render(request, 'chat/index.html', {'username': ' Barnabas'})
