from django.conf.urls import url
from welcome import views

urlpatterns = [
    url(r'^$', views.welcome_view, name='welcome'),
    url(r'^dice/$', views.dice_roll, name='roll_dice'),
    url(r'^api_dice/$', views.api_dice_roll, name='api_roll_dice'),
]
