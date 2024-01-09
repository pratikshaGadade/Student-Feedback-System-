from django.contrib import admin
from django.urls import path
from .views import index,about,contact,register,signin,feedback,course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('course/',course,name="course"),
    path('signin/',signin,name="signin"),
    path('signup/',register,name="signup"),
    path('feedback/',feedback,name="feedback")

]