from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Message, User, UserMessage
from django.contrib.auth import authenticate, login, logout
import random

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.pk)
        if request.POST:
            msg=request.POST['message']
            message=Message.objects.create(user=user, message =msg, writer=user.username )
            message.save()
            user_messages=UserMessage.objects.filter(user_message=msg)
            msg_len=random.randint(0, len(user_messages) -1)
            user_message=user_messages[msg_len]
            # random_reply_message_id_list = random.sample(user_message, min(len(user_message), 1))
            print(user_message)
            
            reply= user_message.reply
            reply_message=Message.objects.create(user=user, message = reply.reply_message)
            reply_message.save()


    
        messages=Message.objects.filter(user = user)
        
        if not messages:
            message=Message.objects.create(user=user, message= "Hey!! How was ur day??"+user.username )
            message.save()
            messages=Message.objects.filter(user = user)
        
        
        return render(request, 'bot.html', context={ 'messages' : messages })
    else:
        return redirect('login')

def loginpage(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['psw']
        user=User.objects.get(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('bot')
        else:
            return render(request, 'login.html', context={'warning': 'Username or password does not match'})

    
    return render(request, 'login.html')
 
def signuppage(request):
    if request.POST:
        user = User() 
        user.username = request.POST['username']
        user.password = request.POST['psw']
        user.age = request.POST['age']
        
        user.save()
        
        return redirect('login')
    
    return render(request, 'signup.html')


def logoutpage(request):
    logout(request)
    return redirect('login')