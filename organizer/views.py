from django.shortcuts import render, get_object_or_404, render_to_response
from django.http.response import HttpResponse, Http404
from django.template import Context, loader, RequestContext

from .models import Tag, Startup

# Create your views here.
def tag_list(request):
    # tag_list = Tag.objects.all()
    # template = loader.get_template(
    #     'organizer/tag_list.html')

    # # RenderContext shortcut, need to pass HTTPRequest object request as parameter
    # context = RequestContext(request, {'tag_list':tag_list})
    # output = template.render(context)
    # return HttpResponse(output)

    # render_to_response shortcut
    #return render_to_response('organizer/tag_list.html', {'tag_list':Tag.objects.all()})

    # render shortcut
    return render(request, 'organizer/tag_list.html', {'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    # template = loader.get_template('organizer/tag_detail.html')
    # context = RequestContext(request, {'tag':tag})
    # return HttpResponse(template.render(context))

    return render(request, 'organizer/tag_detail.html', {'tag':tag})


def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list':Startup.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup':startup})