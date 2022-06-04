import os

from django.http import HttpResponse
from django.shortcuts import render


def salomlash(request):
    return render(request,"salomlash.html")

def oquvchilar(request):
    s  = ["Abdumajid","Jasur","Hoshim","Golib","Shukurullo","Ramziddin","Asadbek","Ali","Jamshid","Javlon","Hadyatilo"]
    return render(request,"oquvchilar.html",{"students":s})

def oquvchi (request,ism):
    s  = ["Abdumajid","Jasur","Hoshim","Golib","Shukurullo","Ramziddin","Asadbek","Ali","Jamshid","Javlon","Hadyatilo"]
    s.remove(ism)
    return render(request,"oquvchi.html",{"students":s})







