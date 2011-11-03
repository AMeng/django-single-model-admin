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

The default changelist view will redirect users to the single object's edit page.
