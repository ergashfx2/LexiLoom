import os

from django.shortcuts import render
from .external import word_definitions, word_synonyms_dict


# Create your views here.

def VocabularyView(request):
    context = {
        'words': word_definitions,
        'synonyms' : word_synonyms_dict
    }
    return render(request, "vocabulary.html", context)


from django.http import JsonResponse
from english_words import get_english_words_set
from .external import get_word
from .models import Word
from gtts import gTTS


#
#

def get_word_definition(request, word):
    tts = gTTS(word, lang='en')
    audio_file_path = os.path.join('static', 'pronunciation.mp3')
    tts.save(audio_file_path)
    word_details = get_word(word)

    context = {
        'audio': audio_file_path,
        'word': word,
        'details': word_details.get('details'),
    }

    return render(request, 'word_detailed.html', context)


def get_english_word_suggestions(request):
    term = request.GET.get('term', '').lower()
    max_suggestions = 15
    word_set = get_english_words_set(['web2'])
    suggestions = [word for word in list(word_set) if term in word][:max_suggestions]
    return JsonResponse(suggestions, safe=False)
