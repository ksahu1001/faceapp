from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .detection import FaceRecognition
from django.contrib.auth.models import User
# from gtts import gTTS
import pyttsx3
import time
import keyboard

faceRecognition = FaceRecognition()


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            addFace(user.id)
            return redirect("/")
        else:
            for msg in form.error_messages:
                messages.info(request, form.error_messages[msg])
    form = UserCreationForm()
    return render(request=request,
                  template_name="register.html",
                  context={"form": form})


def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('/')


def logout_request(request):
    logout(request)
    return redirect("/")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                for msg in form.error_messages:
                    messages.info(request, form.error_messages[msg])
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


def profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()

    return render(request, "profile.html")


def face_login(request):
    user_old = '';
    while True:
        if keyboard.is_pressed('q'):
            break
        face_id = faceRecognition.recognizeFace()
        try:
            user = User.objects.get(id=face_id)
        except User.DoesNotExist:
            user = None
        if user is not None:
            print(user.id)
    
            if(user_old != user.id):
                engine = pyttsx3.init()
                engine.setProperty('rate',120)  #120 words per minute
                engine.setProperty('volume',0.9)
                engine.say("Hello "+  user.first_name + " " + user.last_name + "Welcome to the S R public school") 
                engine.runAndWait()
                
                user_old = user.id
                # time.sleep(5)
