import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from welcome.objects import Dice
from welcome.serializers import DiceSerializer

def welcome_view(request):
    return HttpResponse('Welcome to Grupy-PR!')


def dice_roll(request):
    number = random.randint(1, 6)
    return HttpResponse(number)

@api_view(['GET'])
def api_dice_roll(request):
    n_faces = int(request.GET.get('size', 6))
    dice = Dice(n_faces)
    dice.roll()
    serializer = DiceSerializer(dice)

    return Response(serializer.data)
