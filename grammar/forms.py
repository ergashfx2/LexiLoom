from LexiLoom.grammar.models import Grammar
from django.forms import models


class AddGrammarForm(models.ModelForm):
    class Meta:
        model = Grammar
        fields = '__all__'


class EditGrammarForm(models.ModelForm):
    class Meta:
        model = Grammar
        fields = '__all__'
