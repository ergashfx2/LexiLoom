from django.shortcuts import render

from grammar.models import Grammar


# Create your views here.

def HomePage(request):
    return render(request, template_name="home.html")


def GrammarThemes(request):
    grammar = Grammar.objects.all()
    context = {
        'themes': grammar
    }
    return render(request, template_name="grammar.html",context=context)
