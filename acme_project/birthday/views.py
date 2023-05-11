from pprint import pprint
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from .forms import BirthdayForm
from .models import Birthday
from .utils import get_day_to_brt


def get_page_list(request, page_num):
    template_name = 'birthday/birthday_list.html'
    birthday_list = Birthday.objects.order_by('pk')
    paginator = Paginator(object_list=birthday_list, per_page=10)
    if page_num > paginator.num_pages:
        page_num = 1
    page = paginator.get_page(number=page_num)
    birthday_objects = {
        object: {
            'days_to': get_day_to_brt(object.birthday),
        } for object in page.object_list
    }
    context = {
        'birthday_objects': birthday_objects,
        'paginator': paginator,
    }

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )


def get_list(request):
    """This view function used for show a table of all objects in DataBase."""

    template_name = 'birthday/birthday_list.html'
    birthday_list = Birthday.objects.order_by('pk')
    birthday_objects = {
        object: {
            'days_to': get_day_to_brt(object.birthday),
        } for object in birthday_list
    }
    context = {'birthday_objects': birthday_objects}

    print('*'*50)
    pprint(birthday_list[24].__dict__)
    print('*'*50)
    print(type(birthday_list[24].image))
    print('*'*50)
    pprint(birthday_list[24].image.__dict__)
    print('*'*50)

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

    form = BirthdayForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=object,
    )
    context = {'form': form}

    if form.is_valid():
        form.save()
        if '/create/' in request.path or '/edit/' in request.path:
            id = form.instance.id
            return redirect(to='birthday:preview', pk=id)

    elif '/preview/' in request.path or '/delete/' in request.path:
        for field_class in form.fields.values():
            field_class.widget.attrs['disabled'] = 'disabled'

        if '/preview/' in request.path:
            context['days_to_brt'] = get_day_to_brt(form.initial['birthday'])

        if request.method == 'POST':
            if '/delete/' in request.path:
                object.delete()
            return redirect(to='birthday:list')

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )
