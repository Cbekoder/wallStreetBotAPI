from django.urls import path
from .views import *

urlpatterns = [
    path('levels/', LevelsView.as_view(), name='level-list'),
    path('test/', GetQuizView.as_view(), name='quiz-test'),
    path('check_answers/', CheckAnswersView.as_view(), name='check_answers'),
]