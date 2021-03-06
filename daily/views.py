from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from datetime import datetime
from django.core import serializers
import tweepy
import json
from .models import *
from .forms import *
# Create your views here.


#keys de la API

apiKey = "QIhvFRboJtDHtT17F7DeHnl85"
apiSecretKey =  "twH6KAJlINqoWNfkc8kjYBIyG3I7o5SALzICSjBOD2sngaYlXx"
accesToken = "729986611677671424-tAYmafOvkW9sMHjfG4dc48bruq1dNm2"
accesTokenSecret = "ab6LMT7Uvf6yUfRs05NHHMiUpfFJvA6LMsuff2DqHm0nN"

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accesToken, accesTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

def credential(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'daily/credentials/credential.html')
    
def home(request):
    date = datetime.today().strftime('%m/%d/%Y')
    tweets = Entry.objects.filter(owner = request.user, date = date)[:3]

    mentions = api.mentions_timeline(tweet_mode = "extended")[:3]
    

    return render(request, 'daily/home.html', {
        'tweets': tweets,
        'mentions': reversed(mentions)
    })

def newEntry(request):
    if request.method == 'POST':
        form = entryForm(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            return redirect('home')

    else:
        form = entryForm()
    return render(request, 'daily/newEntry.html', {'form': form})

def delEntry(request, entry_id):
    tweet = Entry.objects.get(id = entry_id)
    tweet.delete()
    return redirect('tweets')

def editEntry(request, entry_id):

    tweet = Entry.objects.get(id= entry_id)
    data = json.loads(request.body)
    tweet.title = data['title']
    tweet.content = data['content']
    tweet.date = data['date']
    tweet.save()
    return JsonResponse(data)

def sendTweet(request, entry_id):

    tweet = Entry.objects.get(id = entry_id)
    tweetMessage = tweet.content
    api.update_status(tweetMessage)

    tweet.delete()

    return redirect('home')


def tweets(request):
    tweets = Entry.objects.filter(owner = request.user)
    return render(request, 'daily/tweets.html', {'tweets': tweets})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, 'daily/credentials/regiter.html', {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'daily/credentials/register', {
                'message': 'Username already taken'
            })

        login(request, user)
        return redirect('home')

    else:
        return render(request, 'daily/credentials/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'daily/credentials/login.html', {
                'message': 'Invalid user and / or password'
            })
    else:
        return render(request, 'daily/credentials/login.html')


def logout_view(request):
    logout(request)
    return redirect('credential')