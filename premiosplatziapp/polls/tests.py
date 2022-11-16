#python
import datetime

#django
from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

#Models
from .models import Question

# Create your tests here.

#Generalmente se hacen tests de:
# Models
# Vistas
class QuestionModelTests(TestCase): #Testeando el modelo "Question"
    def test_was_published_resently_with_future_question(self):
        """
        was_published_recently retorna falso para las preguntas
        en las cuales pub_date estan en el futuro
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text = "Quien es el mejor Course Director de platzi",pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_resently_with_past_question(self):
        """
        was_published_recently retorna False para las preguntas
        en las cuales pub_date estan en el pasado
        """
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(question_text = "Quien es el mejor Course Director de platzi", pub_date = time)
        self.assertIs(past_question.was_published_recently(), False)

    def test_was_published_resently_with_present_question(self):
        """
        was_published_recently retorna True para las preguntas
        en las cuales pub_date estan en el presente
        """
        time = timezone.now()
        present_question = Question(question_text = "Quien es el mejor Course Director de platzi", pub_date = time)
        self.assertIs(present_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Creando una pregunta con el "question_text" dado y con los dias de diferencia
    de publicacion con respecto al dia presente (numeros negativos para las preguntas publicadas en el pasado y numeros positivos para las preguntas que van a ser publicadas en el futuro)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase): #testeando la vista "IndexView"
    def test_no_questions(self):
        """
        Si no existe ninguna pregunta, se mostrara un mensaje apropiado
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_questions(self):
        """
        Questions con un pub_date en el futuro no son mostradas en nuestro index
        """
        create_question("Future question", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_questions(self):
        """
        Questions con un pub_date en el pasado son mostradas en nuetro index
        """
        question = create_question("Past question", -10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_future_question_and_past_question(self):
        """
        Incluso si las questions pasada y futura existen, solo seran mostradas las 
        preguntas en el pasado
        """
        past_question = create_question("Past question", -30)
        future_question = create_question("Future question", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])

    def test_two_past_questions(self):
        """
        La pagina principal puede mostrar multiples preguntas
        """
        
        past_question1 = create_question("Past question 1", -30)
        past_question2 = create_question("Future question 2", -40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question1, past_question2])

    def test_two_future_questions(self):
        future_question1 = create_question("Future question 1", 30)
        future_question2 = create_question("Future question 2", 50)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])