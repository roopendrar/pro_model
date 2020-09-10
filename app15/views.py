from django.shortcuts import render,redirect
from django.http import HttpResponse
from app15.models import *



# Create your views here.

def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h3>Topic Added Successfully</h3>")
        else:
            return HttpResponse("<h3>Topic Is Already Exist In The Table</h3>")

    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get('url')
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h3>Webpage Added Successfully</h3> ")
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={'topics':topics})

def display_topic(request):
    topics=Topic.objects.all()
    return render(request,"display_topic.html",context={"topics":topics})

def display_webpage(request):
    webpage=Webpage.objects.all()
    return render(request,"display_webpage.html",context={"webpage":webpage})

def display_topics(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,"display_topic.html",context={"topics":topics})

def display_webpages(request,id):
    webpage=Webpage.objects.filter(id=id)
    return render(request,"display_webpage.html",context={"webpage":webpage})
    
