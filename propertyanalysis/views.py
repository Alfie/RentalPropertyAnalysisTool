from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from .models import Property

property1 = Property(rental_income=7)
property1.save()

def index(request):
    test = Property.objects.all()
    return render(request, 'propertyanalysis/index.html', {'test': test})
