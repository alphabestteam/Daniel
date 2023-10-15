from django.shortcuts import render
from django.http import HttpResponse
import random


def get_random_number(request):
    random_number = random.randint(0, 1)
    return HttpResponse({'random_number': random_number})

