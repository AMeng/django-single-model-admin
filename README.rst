=========================
DJANGO SINGLE MODEL ADMIN
=========================
A subclass of Django's ModelAdmin for use with models that are only meant to have one record.
This is useful for things like site-wide settings

Usage:
------

Works exactly the same as Django's ModelAdmin


    from singlemodeladmin import SingleModelAdmin

    MyModelAdmin(SingleModelAdmin):
        list_display = [ ... ]

        search_fields = [ ... ]

If there is only one object, the changelist will redirect to that object.
If there are no objects, the changelist will redirect to the add form.
If there are multiple objects, the changelist is displayed with a warning.

Attempting to add a new record when there is already one will result in a
warning and a redirect away from the add form.
