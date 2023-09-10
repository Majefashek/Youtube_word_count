from django.urls import path,include
from .views import wordTranscriptCount

urlpatterns = [
    path('',wordTranscriptCount, name="wordcount")
]
