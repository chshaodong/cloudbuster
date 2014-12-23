cloudbuster
===========
The idea:
Ansible + Celery + Django WebUI = Awesomesauce

A Django app for managing ansible. Jobs are to be queued in AMQP broker, and executed by Celery asynchronously

So far, only module import and viewing a module list in a browser is working. 

Checkout to a virtualenv
`pip install -r requirements.pip`

Run tests:
`./manage.py test`

Setup for development
`./manage.py syncdb --noinput`
`./manage.py load_ansible_modules`
`./manage.py build_module_categories`
`./manage.py runserver`

Point your browser to http://localhost:8000/ansible/modules/
