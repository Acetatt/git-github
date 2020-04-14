from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here.
def homepage(request):
	if request.user.is_authenticated:
		return render(request=request,
		          template_name="main/homepage.html",
		          context = {"Category": Category.objects.all, "info": "logout"}
				  ) 
	return render(request=request,
		          template_name="main/homepage.html",
		          context = {"Category": Category.objects.all, 'info': "Login"}
				  ) 

def contact(request):
	if request.method == "POST":
		contact = request.POST.get('email', "")
		message = request.POST.get('message', "")
		new_message = Message(message_contact=contact, message_content=message)
		new_message.save()
		messages.success(request, "Your message has been sent !")
		return redirect('/')
	return render(request=request,
		          template_name="main/Contact.html"
				  ) 

@login_required(login_url="/Login")
def content(request, num=1):
	return render(request=request,
				  template_name="main/content_spect.html",
				  context={"books": Book.objects.filter(book_category_id=num), "category": Category.objects.all
				  , "owner": Owner.objects.all, "availibility": Book.book_availibility}
				  )

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			login(request, user)
			messages.success(request, f"You are now logged in as: {username}")
			return redirect("/")
		else:
			messages.info(request, "Prout")
			messages.error(request, "Your account cound't be created, try again please")
	form = UserCreationForm
	return render(request,
				  "main/Register.html",
				  context={"form":form}
				  )

@login_required(login_url="/Login")
def logout_a(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect('/')

def login_a(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"You are logged in as: {username}")
				return redirect("/")
			else:
				messages.error(request, "Ah")
		else: 
			messages.error(request, "Username or password is incorrect")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form}
				 )

@login_required(login_url="/Login")
def addi(request):
	messages.success(request, "that's a start")
	if request.POST == "POST":
		message.succes(request, "Au moins t'as fait ton form")
		my_form = (request.POST.get("name", ""), request.POST.get("group2", ""),request.POST.get("group1", ""),request.POST.get("descritpion", ""))
		message.succes(request, "Au moins t'as fait ton form")
		if my_form.is_valid():
			new_Book = Book(book_name=request.POST.get("name", ""),book_owner =request.POST.get("group2", ""), book_availibility="Availible",book_category=request.POST.get("group1", ""), book_description=request.POST.get("descritpion", ""))
			new_Book.save()
			messages.succes(request, "The book was successfully added")
			return redirect("/")
		else:
			message.error(request, "t'as faux sale merde")
			return redirect("/")
	return render(request=request,
				  template_name="main/add.html",context={"category": Category.objects.all
				  ,"owner": Owner.objects.all}
				  )

											
@login_required(login_url="/Login")
def update(request, num=1):
	pass

@login_required(login_url="/Login")
def delete(request):
	pass

 

