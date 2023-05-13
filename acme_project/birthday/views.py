from pprint import pprint
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DeleteView, DetailView, UpdateView
)

from .forms import BirthdayForm
from .models import Birthday
from .utils import get_day_to_brt


class BirthdayMixin:
    model = Birthday


class BirthdayListView(BirthdayMixin, ListView):
    """This view class used for show a table of all objects in DataBase."""

    # model = Birthday
    ordering = 'pk'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.context_data['object_list'] = {
            object: {
                'days_to_brt': get_day_to_brt(object.birthday)
            } for object in response.context_data.get('object_list')
        }
        return response


class BirthdayDetailView(BirthdayMixin, DetailView):
    """This view class used for preview object in DataBase via ModelForm."""

    # model = Birthday

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        object = response.context_data.get('object')
        form = BirthdayForm(instance=object)

        for key, field in form.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
        response.context_data['form'] = form
        response.context_data['days_to_brt'] = get_day_to_brt(object.birthday)
        return response


class BirthdayCreateView(BirthdayMixin, CreateView):
    """This view class used for create object in DataBase via ModelForm."""

    # model = Birthday
    # form_class = BirthdayForm
    fields = ['first_name', 'last_name', 'birthday']
    # success_url = reverse_lazy('birthday:list')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    """This view class used for update object in DataBase via ModelForm."""

    # model = Birthday
    form_class = BirthdayForm
    # success_url = reverse_lazy('birthday:list')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    """This view class used for delete object in DataBase via ModelForm."""

    # model = Birthday
    success_url = reverse_lazy('birthday:list')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        object = response.context_data.get('object')
        form = BirthdayForm(instance=object)

        for key, field in form.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
        response.context_data['form'] = form
        return response
