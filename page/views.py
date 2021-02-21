from django.shortcuts import render, redirect
from page.models import Message

# Create your views here.
def get_index(request):
    return render(request, 'home.html')

def post_message(request):
    messages = Message.objects.all()
    print(messages) # standard IO코드는 빼주세요 :)(
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        newMessage = Message(name = name, message = message)
        newMessage.save()
        return redirect('/more#messages')
    return render(request, "more.html", {'messages':messages})
