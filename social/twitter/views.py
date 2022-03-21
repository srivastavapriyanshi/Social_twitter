from django.shortcuts import render
from .models import Profile, Tweets
from django.shortcuts import  render, redirect
from .forms import NewUserForm, PostTweetForm
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpResponseRedirect


# Create your views here.
from django.shortcuts import render

def dashboard(request):
    return render(request, "base.html")

def profile(request):
    profile = Profile.objects.get(user=request.user)
    following_count = profile.follows.all().count()
    follower_count = profile.followed_by.all().count()
    return render(request, "twitter/profile.html", {"profile": profile,"following_count":following_count, "follower_count":follower_count})

def main(request):
    return render(request, "index.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("twitter:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("twitter:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("twitter:login")

def post_tweet(request):
	if request.method == "POST":
		form = PostTweetForm(request.POST, request.FILES)
		if form.is_valid():
			obj = Tweets(attachment = request.FILES['attachment'], user= request.user, description = request.get("description"))
			obj.save()
			return HttpResponseRedirect("/homepage/")
	form = PostTweetForm()
	return render(request=request, template_name="post_tweet.html", context = {"login_form":form})
