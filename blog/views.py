from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator


# Create your views here.
#def post_list(request):
    #return render(request, 'blog/post_list.html',{})

class HomeView(ListView):
    model = Post
    paginate_by = 1
    template_name = 'post_list.html'



    