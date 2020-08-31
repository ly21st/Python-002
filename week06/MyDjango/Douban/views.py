from django.shortcuts import render

# Create your views here.
from .models import T1

def books_short(request):
    ###  从models取数据传给template  ###
    condtions = {'n_star__gt': 3}
    shorts = T1.objects.all().filter(**condtions)
    return render(request, 'index.html', locals())