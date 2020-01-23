from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from . models import Property

def index(request):
    return render(request, 'propertyanalysis/index.html')

def calc(request):
    property1 = Property(rental_income=request.POST['rincome'])
    property1.save()
    test = property1
    context = {'test' : test}
    return render(request, 'propertyanalysis/index.html', context)
