=====================
Django bootatrap form
=====================

Generate twitter-bootstrap form output for django form

A django template tag to work with twitter bootstrap ( http://twitter.github.com/bootstrap/ )


Installation
============


``$ pip install django-bootstrap-form``

for people who still use older version before twitter bootstrap 2.0


``$ pip install django-bootstrap-form==0.2``



Configuration
==============

Add 'bootstrapform' to INSTALLED_APPS.


Usage
=====

{% load bootstrap %}

{{ form|bootstrap }}

{{ form.<field name>|bootstrap:"css_class1 css_class2" }} - To output individual fields and add css classes to the input/textarea/select
