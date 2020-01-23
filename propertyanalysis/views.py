from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

def index(request):
    test = request.POST['rincome']
    context = {'test' : test}
    return render(request, 'propertyanalysis/index.html', context)
