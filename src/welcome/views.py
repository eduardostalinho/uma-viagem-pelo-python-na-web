import random
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse('Welcome to Grupy-PR!')


def dice_roll(request):
    number = random.randint(1, 6)
    return HttpResponse(number)

