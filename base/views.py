from django.shortcuts import render, redirect   
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic, Message
from .forms import RoomForm


# Create our view here!
# Login User !
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'user does not exist!')    
            
        user = authenticate(request, username=username, password=password)     
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exits!')
            
    context = {'page':page}
    return render(request, 'base/login_register.html', context)



# LogOut User !
def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')



# Registor User !
def registerUser(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured during registration!')
    
    return render(request, 'base/login_register.html', {'form':form}) 




# Searching For Rooms ! 
def search_rooms(request):
    query = request.GET.get('q') if request.GET.get('q') else ''
    
    rooms = Room.objects.filter(
        Q(name__icontains=query) |  
        Q(description__icontains=query) |  
        Q(host__username__icontains=query) |  
        Q(topic__name__icontains=query)  
    )
    
    context = {'rooms': rooms, 'query':query}
    return render(request, 'base/home.html', context)



# Home !
def home(request):
    query = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(name__icontains=query)  
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=query))
    topics = Topic.objects.all()


    context = {
        'rooms': rooms,
        'topics': topics,
        'query': query,
        'room_count':room_count,
        'room_messages':room_messages,
        'topics':topics, 
    }
    return render(request, 'base/home.html', context)


# PRofile ! Login Required for User !
@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)  
    rooms = user.room_set.all()  
    context = {'user': user, 'rooms': rooms} 
    return render(request, 'base/profile.html', context)


# Room ! Login Required for User !
@login_required(login_url='login')
def room(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return redirect('home')
    room_messages = Message.objects.filter(room=room)
    
    if request.user.is_authenticated:
        room.participants.add(request.user)
    participants = room.participants.all()

    if request.method == 'POST':
        body = request.POST.get('body')
        # Create a new message linked to the user and the room
        message = Message.objects.create(
            user=request.user,  # Automatically link the message to the logged-in user
            room=room,
            body=body
        )        
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants':participants,}
    return render(request, 'base/room.html', context)



# Room CReation ! Login Required for User !
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save() 
            return redirect('home')           
    context = {'form':form}
    return render(request, 'base/room_form.html' , context)



# Room Updation ! Login Required for User !
@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('YOU ARE NOT ALLOWED HERE!')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'base/room_form.html', context)
    
    
    
# Room Deletion ! Login Required for User !   
@login_required(login_url='login')    
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
        
    context = {
        'obj':room,
        'previous_page': request.GET.get('next', 'home')
        }   
    return render(request, 'base/delete.html', context) 
    
    
    
# Message Deletion ! Login Required for User !    
@login_required(login_url='login')    
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse('You are not allowed here!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
        
    context = {
        'obj':message,
        'previous_page': request.GET.get('next', 'home')
        }   
    return render(request, 'base/delete.html', context)     
    
@login_required(login_url='page')        
def updateUser(request):
    return render(request, 'base/updateUser.html', {})