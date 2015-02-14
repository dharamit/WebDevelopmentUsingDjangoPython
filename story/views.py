from django.shortcuts import render_to_response
from story.models import posts
# Create your views here.


############################ /home
def home(request):
	entries = posts.objects.all()#[:5]
	#posts = {'author':'amit','title':'book1'}
	return render_to_response('index.html',{'posts':entries})

def home1(request):
	entries = posts.objects.all()
	return render_to_response('index2.html',{'posts':entries})

def home3(request):
	entries = posts.objects.all()
	return render_to_response('index3.html',{'posts':entries})

def postPost(request):
	post = posts(request.POST)
	post.save()
	entries = posts.objects.all()
	return render_to_response('index3.html',{'posts':entries})