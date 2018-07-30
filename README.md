Django Single ModelAdmin
========================

[![PyPI Version](https://img.shields.io/pypi/v/singlemodeladmin.svg)][pypi]
[![Build Status](http://img.shields.io/travis/AMeng/django-single-model-admin.svg)][travis]

[travis]: http://travis-ci.org/AMeng/django-single-model-admin
[pypi]: https://pypi.python.org/pypi/singlemodeladmin

A subclass of Django's `ModelAdmin` for use with models that are only meant to
have one record. This is useful for things like site-wide settings.

Usage:
------

Register a model with `SingleModelAdmin`:

```python
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from my_app.models import MyModel

admin.site.register(MyModel, SingleModelAdmin)
```
You can also subclass `SingleModelAdmin` instead of Django's `ModelAdmin`, and
it will work as expected:

```python
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from my_app.models import MyModel

class MyModelAdmin(SingleModelAdmin):
    list_display = ['my_field']

admin.site.register(MyModel, MyModelAdmin)
```

Installation:
-------------
```
pip install singlemodeladmin
```

Behavior:
---------

 * If there is only one object, the changelist will redirect to that object.
 * If there are no objects, the changelist will redirect to the add form.
 * If there are multiple objects, the changelist is displayed with a warning
 * Attempting to add a new record when there is already one will result in a
   warning and a redirect away from the add form.

Supported Django Versions:
--------------------------
 * 1.4
 * 1.5
 * 1.6
 * 1.7
 * 1.8
 * 1.9
 * 1.10
 * 1.11
 * 2.0

Supported Python Versions:
--------------------------
 * 2.6
 * 2.7
 * 3.3
 * 3.4
 * 3.5
 * 3.6
 * 3.7
