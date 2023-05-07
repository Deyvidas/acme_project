from django.shortcuts import get_object_or_404, redirect, render

from .forms import BirthdayForm
from .models import Birthday
from .utils import get_day_to_brt, get_form_fields_attribute


def get_list(request):
    """This view function used for show a table of all objects in DataBase."""

    template_name = 'birthday/birthday_list.html'
    birthday_list = Birthday.objects.all()
    birthday_objects = {
        object: {
            'days_to': get_day_to_brt(object.birthday)
        } for object in birthday_list
    }
    context = {'birthday_objects': birthday_objects}

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )


def crude_birthday(request, pk=None):
    """
    This view function used for create, read, update, delete
    objects in DataBase via ModelForm class.
    """

    template_name = 'birthday/birthday.html'
    object = None

    if pk:
        object = get_object_or_404(klass=Birthday, pk=pk)

    form = BirthdayForm(data=request.POST or None, instance=object)
    context = {'form': form, 'inactive_attrs': None}

    if form.is_valid():
        form.save()
        if '/preview/' in request.path:
            return redirect(to='birthday:list')
        elif '/create/' in request.path or '/edit/' in request.path:
            id = form.instance.id
            return redirect(to='birthday:preview', pk=id)

    elif f'/{pk}/preview/' in request.path or f'/{pk}/delete/' in request.path:
        context['inactive_attrs'] = get_form_fields_attribute(form=form)

        if f'/{pk}/preview/' in request.path:
            context['days_to_brt'] = get_day_to_brt(form.initial['birthday'])

        if request.method == 'POST':
            if f'/{pk}/delete/' in request.path:
                object.delete()
            return redirect(to='birthday:list')

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )
