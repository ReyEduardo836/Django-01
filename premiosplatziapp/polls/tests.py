#python
import datetime

#django
from django.test import TestCase
from django.utils import timezone

#Models
from .models import Question

# Create your tests here.

#Generalmente se hacen tests de:
# Models
# Vistas
class QuestionModelTests(TestCase):
    def test_was_published_resently_with_future_question(self):
        """
        was_published_recently retorna falso para las preguntas
        en las cuales pub_date estan en el futuro
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text = "Quien es el mejor Course Director de platzi",pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)