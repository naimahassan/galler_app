from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image,Location,Category

def welcome(request):

    pics = Image.objects.all()
    return render(request,'welcome.html', {"pics":pics})

def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()    

    return render(request,"all-pics/image.html",{"image":image})

# def get_image(request,image_id):
#     image = Image.get_image(image_id)
#     return render(request,'all-pics/image.html',{"pics":pics})

def search_results(request):
    if 'pics' in request.GET and request.GET["pics"]:
        query = request.GET.get("pics")
        search_results = Image.searched(query)
        message =f"{query}"

        return render(request, 'all-pics/search.html', {"message":message,"results":search_results})

    else:
        message = "no searched term"
        return render(request,'all-pics/search.html',{"message":message})    

def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url

# def filter_location(request,id):
#     images= Image.filter_by_location(id= location.id)
#     return render(request,'filter.html',{"images":images})
