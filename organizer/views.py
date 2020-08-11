from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Tag

# Create your views here.
def homepage(request):
    tag_list = Tag.objects.all()
    output = ", ".join(tag.name for tag in tag_list)
    return HttpResponse(output)