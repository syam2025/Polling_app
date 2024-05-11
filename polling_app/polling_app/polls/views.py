from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import PollForm, VoteForm
from .models import Poll, Choice

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
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
            poll.owner = request.user
            poll.save()
            choices = [form.cleaned_data.get('choice1'), form.cleaned_data.get('choice2'), form.cleaned_data.get('choice3')]
            for choice_text in choices:
                if choice_text:
                    Choice.objects.create(poll=poll, choice_text=choice_text)
            return redirect('home')
    else:
        form = PollForm()
    return render(request, 'polls/create_poll.html', {'form': form})

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        form = VoteForm(request.POST, poll=poll)
        if form.is_valid():
            choice_id = form.cleaned_data['choice_text'].id
            selected_choice = poll.choice_set.get(pk=choice_id)
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('home')
    else:
        form = VoteForm(poll=poll)
    return render(request, 'polls/vote.html', {'poll': poll, 'form': form})


