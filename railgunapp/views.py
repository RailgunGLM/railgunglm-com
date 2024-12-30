from django.shortcuts import render
from .models import Post, Settings, Answer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def index(request):
    return render(request, 'railgunapp/index.html')

def blog(request):
    get_all_posts = Post.objects.all()
    context = {
        'posts': get_all_posts
    }
    return render(request, 'railgunapp/blog.html', context)

def blogDetail(request, slug):
    get_post = Post.objects.get(slug=slug)
    context = {
        'post': get_post
    }
    return render(request, 'railgunapp/blog/article.html', context)

def bio(request):
    return render(request, 'railgunapp/bio.html')

def project(request):
    return render(request, 'railgunapp/project.html')

@csrf_exempt
def dseictool(request):
    print(request.POST)
    freq = len(Settings.objects.all())
    context = {
        'freq': freq,
    }
    if request.method == "POST" and request.POST.get('button') == "start":
        module = request.POST.get('module')
        topic = request.POST.get('topic')
        qno = request.POST.get('qno')
        settings = Settings(module=module, topic=topic, qno=str(qno))
        settings.save()
        return HttpResponse('')
    elif request.method == "POST" and request.POST.get('question') != None and request.POST.get('answer') != None:
        question = request.POST.get('question')
        ans = request.POST.get('answer')
        answer = Answer(question=question, answer=ans)
        answer.save()
        return HttpResponse('')
    return render(request, 'railgunapp/project/dseictool.html', context)