from django.shortcuts import render
from .models import Poem
# Create your views here.
def poemlist(request):
	return render(request, 'home.html', {'poems':Poem.objects.all()})
