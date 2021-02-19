from django.shortcuts import render, redirect
from page.models import Message

# Create your views here.
def home(request):
    return render(request, 'home.html')

def more(request):
    messages = Message.objects.all()
    print(messages)
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        newMessage = Message(name = name, message = message)
        newMessage.save()
        return redirect('/more#messages')
    return render(request, "more.html", {'messages':messages})
