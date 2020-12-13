from django.http import HttpResponse


# Create your views here.

def addPageView(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    result = first+second
    return HttpResponse(result)
	

def multiplyPageView(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    result = first*second
    
    return HttpResponse(result)
