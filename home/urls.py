from django.urls import path
from .views import HomePage
from .views import GrammarThemes

urlpatterns = [
    path("", HomePage, name="home"),
    path('grammar', GrammarThemes, name='grammar')
]
