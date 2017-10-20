from django.contrib import admin, messages
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import redirect
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse


class SingleModelAdmin(admin.ModelAdmin):

    """
    Django ModelAdmin for models that are only meant to have one record.
    This is useful for a site-wide settings model, among other things.

    If there is only one object, the changelist will redirect to that object.
    If there are no objects, the changelist will redirect to the add form.
    If there are multiple objects, the changelist is displayed with a warning.

    Attempting to add a new record when there is already one will result in a
    warning and a redirect away from the add form.
    """

    def _get_model_name(self):
        try:
            return self.model._meta.model_name
        except AttributeError:
            return self.model._meta.module_name

    def changelist_view(self, request, extra_context=None):
        app_and_model = '{0}_{1}'.format(self.model._meta.app_label,
                                         self._get_model_name())
        try:
            instance = self.model.objects.get()
        except self.model.DoesNotExist:
            return redirect(reverse('admin:{0}_add'.format(app_and_model)))
        except MultipleObjectsReturned:
            warning = ('There are multiple instances of {0}. There should only'
                       ' be one.').format(self._get_model_name())
            messages.warning(request, warning, fail_silently=True)
            return super(SingleModelAdmin, self).changelist_view(
                request, extra_context=extra_context)
        else:
            return redirect(reverse('admin:{0}_change'.format(app_and_model),
                                    args=[instance.pk]))

    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count():
            warning = ('Do not add additional instances of {0}. Only one is'
                       ' needed.').format(self._get_model_name())
            messages.warning(request, warning, fail_silently=True)
            return redirect(reverse('admin:{0}_{1}_changelist'.format(
                self.model._meta.app_label,
                self._get_model_name())))
        return super(SingleModelAdmin, self).add_view(
            request,
            form_url=form_url,
            extra_context=extra_context)

    def has_add_permission(self, request):
        try:
            self.model.objects.get()
        except self.model.DoesNotExist:
            return super(SingleModelAdmin, self).has_add_permission(request)
        except MultipleObjectsReturned:
            pass
        return False
