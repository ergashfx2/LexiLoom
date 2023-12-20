from django.contrib import admin
from .models import Grammar
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin


class GrammarAdmin(SummernoteModelAdmin):
    summernote_fields = 'description'


admin.site.register(Grammar, GrammarAdmin)
