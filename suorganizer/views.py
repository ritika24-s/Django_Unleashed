# from django.http import HttpResponseRedirect

# def redirect_root(request):
#     return HttpResponseRedirect('/blog/')

from django.shortcuts import redirect 

def redirect_root(request):
    return redirect('blog_post_list')