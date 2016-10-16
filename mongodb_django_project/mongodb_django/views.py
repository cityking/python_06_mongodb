# encoding:utf-8
from django.shortcuts import render,HttpResponseRedirect
from mongodb_django.models import Poem

# Create your views here.
def add(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		author = request.POST.get('author')
		poem = Poem(title=title,author=author)
		poem.tag='tag'
		poem.save()
		return HttpResponseRedirect('/')
	else:
		return render(request, 'add.html')
def home(request):
	return render(request, 'home.html', {'showtitle':'所有诗词信息','poems':Poem.show_news()})

def update(request):
	if request.method == 'POST':
		id = request.POST.get('id')
		author = request.POST.get('author')
		title = request.POST.get('title')
		poems = Poem.objects(poem_id=id)
		for poem in poems:
			#poem.author=author
			#poem.title=title
			#poem.save()
			poem.update(title=title, author=author)
		return HttpResponseRedirect('/')
	else:
		return render(request,'update.html')
	
def delete(request):
	if request.method == 'POST':
		id = request.POST.get('id')
		poems = Poem.objects(poem_id=id)
		for poem in poems:
			poem.delete()
		return HttpResponseRedirect('/')
	else:
		return render(request,'delete.html')

