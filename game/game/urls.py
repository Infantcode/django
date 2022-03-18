from game.views import index,play
from django.urls import path

urlpatterns = [
        path("", index, name = "index"), 
        path("play/",play,name="play"),
        ]
