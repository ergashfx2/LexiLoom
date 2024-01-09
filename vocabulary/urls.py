from django.urls import path
from .views import VocabularyView,get_english_word_suggestions,get_word_definition

urlpatterns = [
    path("vocabulary", VocabularyView, name='vocabulary'),
    path('get_english_word_suggestions/', get_english_word_suggestions, name='get_english_word_suggestions'),
    path('get_word_definition/<slug:word>/', get_word_definition, name='get_word_definition'),

]
