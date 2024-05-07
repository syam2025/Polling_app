from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import PollForm, ChoiceForm
from .models import Poll

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'polls/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'polls/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    polls = Poll.objects.all()
    return render(request, 'polls/home.html', {'polls': polls})

def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            return redirect('home')
    else:
        form = PollForm()
    return render(request, 'polls/create_poll.html', {'form': form})

def vote(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = poll.choice_set.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('home')
    return render(request, 'polls/vote.html', {'poll': poll})

