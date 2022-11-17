# Creando un proyecto en Django - Python
1. creamos un entorno virtual 
```sh
python3 -m venv venv
```
2. activamos el entorno virtual 
```sh
source ./venv/bin/activate
```
3. Instalar Django
```sh
sudo pip install django
```
4. Agregando requirements.txt
```sh
pip freeze > requirements.txt
```
5. para instalar los paquetes dentro de requirements.txt
```sh
pip install -r requirements.txt
```
6. Iniciamos el proyecto de django
```sh
django-admin startproject premiosplatziapp
```
7. corremos el servidor local
```sh
cd premiosplatziapp
python3 manage.py runserver
```
8. Creando una app dentro del proyecto premiosplatziapp
```sh
cd premiosplatziapp
python3 manage.py startapp polls
```
9. Hacemos una migracion de "polls" para mapear nuestros modelos a la base de datos
```sh
cd premiosplatziapp
python3 manage.py makemigrations polls
python3 manage.py migrate
```
10. Agregando una "Question" a la base de datos con la consola de Django
```sh
python3 manage.py shell
` `
>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> q = Question(question_text="Cual es el mejor curso de Platzi?", pub_date=timezone.now())
>>> q.save()
```
11. Consultando el dato con un PrimaryKey = 1 desde la consola de Django
```sh
python3 manage.py shell
` `
>>> from polls.models import Question, Choice
>>> Question.objects.get(pk=1)
<Question: Cual es el mejor curso de Platzi?>
```
12. Consultando una lista de datos con filter() desde la consola de Django
```sh
>>> Question.objects.filter(question_text__startswith="Cual")
<QuerySet [<Question: Cual es el mejor curso de Platzi?>,
	<Question: Cual es la mejor escuela de platzi?>]>
>>> Question.objects.filter(pub_date__year=timezone.now().year)
<QuerySet [<Question: Cual es el mejor curso de Platzi?>,
	<Question: Quien es el mejor profesor de platzi?>,
	<Question: Cual es la mejor escuela de platzi?>]>
```
13. Creando respuestas a la pregunta creada anteriormente desde la consola de Django
```sh
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
```
14. Creando un superUsuario para poder entrar a Django Admin
```sh
python3 manage.py createsuperuser
```

## PYTHON INTERMEDIO
15. ejecutando el comando para los tests ubicados en polls
```sh
python3 manage.py test polls
```
>Recordar que los tests se ejecutan con una base de datos temporal que se crea al 
>iniciar los tests y se destruye al finalizarlos (no toma en cuenta la base de datos
>de nuestro proyecto)
