
# apps/konnected/learning/views.py

from rest_framework import viewsets, permissions
from apps.konnected.learning.models import Lesson, Quiz, Question, Answer
from apps.konnected.learning.serializers import (
    LessonSerializer,
    QuizSerializer,
    QuestionSerializer,
    AnswerSerializer
)

class LessonViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les leçons interactives.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuizViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les quiz associés aux leçons.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les questions des quiz.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnswerViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les réponses aux questions.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
