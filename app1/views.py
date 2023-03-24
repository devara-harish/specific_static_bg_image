from django.shortcuts import render

# Create your views here.
def bg_image(request):
    return render(request,'bg_image.html')