from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>fuck yea</h1>")
