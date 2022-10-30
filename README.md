1. creamos un entorno virtual 
python3 -m venv venv
2. activamos el entorno virtual 
source ./venv/bin/activate
3. Instalar Django
sudo pip install django
4. Iniciamos el proyecto de django
django-admin startproject premiosplatziapp
5. corremos el servidor local
cd premiosplatziapp
python3 manage.py runserver
6. Creando una app dentro del proyecto premiosplatziapp
cd premiosplatziapp
python3 manage.py startapp polls
7. Hacemos una migracion de "polls" para mapear nuestros modelos a la base de datos
cd premiosplatziapp
python3 manage.py makemigrations polls
python3 manage.py migrate
8. Agregando una "Question" a la base de datos con la consola de Django
python3 manage.py shell

>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> q = Question(question_text="Cual es el mejor curso de Platzi?", pub_date=timezone.now())
>>> q.save()
9. Consultando el dato con un PrimaryKey = 1 desde la consola de Django
python3 manage.py shell

>>> from polls.models import Question, Choice
>>> Question.objects.get(pk=1)
<Question: Cual es el mejor curso de Platzi?>
10. Consultando una lista de datos con filter() desde la consola de Django
>>> Question.objects.filter(question_text__startswith="Cual")
<QuerySet [<Question: Cual es el mejor curso de Platzi?>,
	<Question: Cual es la mejor escuela de platzi?>]>
>>> Question.objects.filter(pub_date__year=timezone.now().year)
<QuerySet [<Question: Cual es el mejor curso de Platzi?>,
	<Question: Quien es el mejor profesor de platzi?>,
	<Question: Cual es la mejor escuela de platzi?>]>
11. Creando respuestas a la pregunta creada anteriormente desde la consola de Django
>>> q = Question.objects.get(pk=1)
>>> q.choice_set.create(choise_text="Curso Basico de Python", votes=0)
<Choice: Curso Basico de Python>
>>> q.choice_set.create(choise_text="Curso de Fundamentos de Ingenieria de Software", votes=0)
<Choice: Curso de Fundamentos de Ingenieria de Software>
>>> q.choice_set.create(choise_text="Curso de Elixir", votes=0)
<Choice: Curso de Elixir>
>>> q.choice_set.all()
<QuerySet [<Choice: Curso Basico de Python>,
	<Choice: Curso de Fundamentos de Ingenieria de Software>,
	<Choice: Curso de Elixir>]>
>>> q.choice_set.count()
3
>>> Choice.objects.filter(question__pub_date__year=timezone.now().year)
<QuerySet [<Choice: Curso Basico de Python>, <Choice: Curso de Fundamentos de Ingenieria de Software>, <Choice: Curso de Elixir>]>
