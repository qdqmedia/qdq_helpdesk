qdq-helpdesk - A HelpDesk application
======================================

HelpDesk application by QDQ Media.

Licensing
---------

This project is based on `django-helpdesk <https://github.com/rossp/django-helpdesk>`_, see
license details `here <https://github.com/rossp/django-helpdesk/blob/master/LICENSE>`_.

Installation
-------------

1. Clone this project.

2. Execute::

    $ pip install -r requirements/project.txt

3. For development environments::

    $ pip install -r requirements/dev.txt

3. Sync. database::

    $ python manage.py syncdb
    $ python manage.py migrate
