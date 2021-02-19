from django.shortcuts import render
from math import acos
def home(requests):
    lis=[i for i in range(51)]
    return render(requests,"genrator/home.html",{'lis':lis})

def output(requests):
    length=requests.GET.get('length')
    float = '{:.' + str(length) + 'f}'
    pi_value = float.format(2 * acos(0.0))
    return render(requests,"genrator/output.html",{'pi_value':pi_value})
