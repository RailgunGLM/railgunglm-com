from django.shortcuts import render
from app import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    context={}
    return render(request, "app/index.html", context)

def bio(request):
    context={}
    return render(request, "app/bio.html", context)

def blog(request):
    context={}
    return render(request, "app/blog.html", context)

def project(request):
    context={}
    return render(request, "app/project.html", context)

@csrf_exempt
def dseictool(request):
    print(request.POST)
    if request.method == 'POST' and request.POST.get('button') == 'start':
        module = request.POST.get('module')
        topic = request.POST.get('topic')
        question = request.POST.get('qno')
        if module != 'Select module' and topic != 'Select topic' and question != 'Select number of questions':
            models.insert_record(module, topic, question)
        return HttpResponse('')
    elif request.method == 'POST' and request.POST.get('answer') != None:
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        models.insert_answer(question, answer)
        return HttpResponse('')
    setting_data = models.get_setting()
    return render(request, "app/project/dseictool.html", {'count': len(setting_data)})