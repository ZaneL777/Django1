from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def blogs(request):
    blogs = blogs.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'blogs': blogs,
  }
    return HttpResponse(template.render(context, request))