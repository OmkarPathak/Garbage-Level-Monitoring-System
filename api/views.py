from django.shortcuts import redirect

# Create your views here.
from .models import Readings


def add_entry(request, id, level):
    api_add = Readings(dustbin_id=id, level=level)
    api_add.save()
    return redirect('/dashboard')
