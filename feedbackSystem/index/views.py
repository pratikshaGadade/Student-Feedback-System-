from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm,FeedbackEntry
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def course(request):
    return render(request,'course.html')



def register(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/signin")
    else:
        fm=SignupForm()
    return render(request,"Register.html",{'form':fm})

def signin(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return render(request, 'feedback.html',{'user':user})
                return redirect("/feedback")

    else:
        fm = AuthenticationForm()
    return render(request,"signin.html",{'form':fm})


def feedback(request):
    if request.method=="POST":
        fm=FeedbackEntry(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/feedback')

    else:
        fm=FeedbackEntry()
    return render(request, 'feedback.html', {'form': fm})



# Create your views here.
