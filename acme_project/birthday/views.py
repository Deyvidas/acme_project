from django.shortcuts import render

from .forms import BirthdayForm
from .utils import get_day_to_brt


def birthday(request):

    template_name = 'birthday/birthday.html'
    form = BirthdayForm(request.GET or None)
    context = {
        'form': form,
    }

    if form.is_valid():
        birth_date = form.cleaned_data.get('birthday')
        context['birthday_countdown'] = get_day_to_brt(birth_date)

    return render(request=request,
                  template_name=template_name,
                  context=context)
