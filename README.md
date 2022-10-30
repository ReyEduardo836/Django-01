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
