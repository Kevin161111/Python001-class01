from django.shortcuts import render
from .models import T1 
from django.db.models import Avg
# Create your views here.

def index(request,):
    shorts = T1.objects.all()
    counter = T1.objects.all().count()

    star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # 展示高于3星级（不包括3星级）的短评内容和它对应的星级

    queryset = T1.objects.all()
    conditions = {'n_star__gt':3}
    filter_shorts = queryset.filter(**conditions).all()[:20]

    return render(request,'result.html',locals())

