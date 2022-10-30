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
