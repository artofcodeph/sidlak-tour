from django.shortcuts import render
from django.http import HttpResponse
from .models import Guide


# Create your views here. equivalent controller 
def index(request):

    guides = Guide.objects.all()

    context = {
        'tour_guides': guides
    }

    # return HttpResponse("<h1>Hello Sidlak!</h1>")
    return render(request, 'tour_guides/index.html', context)
