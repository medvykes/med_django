from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('speeches/', views.SpeechListView.as_view(), name = 'speech_list'),
    path('speeches/<int:speech_id>/', views.SpeechDetailView.as_view(), name = 'speech_detail'),
    path('speakers/', views.SpeakerListView.as_view(), name = 'speaker_list'),
    path('speaker/<int:speaker_id>/', views.SpeakerDetailView.as_view(), name = 'speaker_detail'),
    #path('speech/<speaker-id>/create/', , name = 'comments'),
    #path('accounts/<standardurls>/', , name = 'auth'),
]