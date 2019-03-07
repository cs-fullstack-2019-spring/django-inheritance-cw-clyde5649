from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# the page the user sees

#def index(request):
 #   return HttpResponse('Call me')


def index(request):
    return render(request, 'CodeCrewApp/index.html')



def aboutus(request):
    return render(request, 'CodeCrewApp/aboutus.html')




def contactus(request):
    return render(request, 'CodeCrewApp/contactus.html')



def gallery(request):
    return render(request, 'CodeCrewApp/gallery.html')



def resources(request):
    return render(request, 'CodeCrewApp/resources.html')