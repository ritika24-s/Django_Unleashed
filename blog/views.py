from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.decorators.http import require_http_methods

from .models import Post

# function based view
# def post_list(request):
#     return render(request, 'blog/post_list.html', {'post_list':Post.objects.all()})

# class based view
class PostList(View):
    def get(self, request):
        return render(request, 'blog/post_list.html', {'post_list':Post.objects.all()})

@require_http_methods(['HEAD','GET'])
def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post})