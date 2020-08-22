from django.shortcuts import render, redirect
from . models import Article
from django.views.generic import CreateView

# Create your views here.

def home(request):
	context = {

	'art': Article.objects.all()

	}
	
	return render(request, 'blog/home.html', context)


class NewPost(CreateView):
	model = Article
	template_name = 'blog/post.html'
	fields = '__all__'