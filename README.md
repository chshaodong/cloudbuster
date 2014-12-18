cloudbuster
===========
The idea:
Ansible + Celery + WebUI = Awesomesauce

A Django app for managing ansible. Jobs are to be queued in AMQP broker, and executed by Celery asynchronously

So far, only module import and viewing a module list in a browser is working. 

Checkout to a virtualenv
pip install -r requirements.pip

./manage.py syncdb
./manage.py load_ansible_modules
./manage.py runserver

Point your browser to http://localhost:8000/ansible/modules/
