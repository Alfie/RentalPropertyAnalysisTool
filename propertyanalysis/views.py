from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from .models import Property

def index(request):
    test = Property.objects.all()
    context = {'test': test}
    return render(request, 'propertyanalysis/index.html', context)

def edit(request):
    p2 = Property(rental_income=request.POST['rincome'])
    p2.save()
    test = Property.objects.all()
    context = {'test': test}
    return render(request, 'propertyanalysis/edit.html', context)
