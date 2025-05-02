# voicebot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.voice),
    path('generate-voice/', views.generate_voice, name='generate_voice'),
]
