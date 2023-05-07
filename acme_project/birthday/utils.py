from datetime import date

from django.forms import ModelForm


def get_day_to_brt(birth_date: date) -> int:
    """Возвращает количество дней до дня рождения."""
    today = date.today()
    brday = birth_date
    tod_y = today.year
    brt_m = brday.month
    brt_d = brday.day
    days_to_brtday = (date(tod_y, brt_m, brt_d) - today).days

    if days_to_brtday < 0:
        days_to_brtday = (date(tod_y+1, brt_m, brt_d) - today).days
    return days_to_brtday


def get_form_fields_attribute(form: ModelForm) -> dict:
    """
Возвращает словарь где:
    - ключ — это атрибут name тега input
    - значение — это словарь с остальными атрибутами тегов формы:
    > Для тега label
        * label — это значение внутри тега label
        * str_value — это нормализированное значение заполненного поля преобр. в str
        * value — это нормализированное значение заполненного поля
    > Для тега input
        * input_id — это атрибут id тега input
        * type — это атрибут type тега input
        * is_required — это булево значение является ли тег input обязательным
    > Для тега отвечающего за help_text
        * help_text — это значение внутри тега для подсказки к полю
    """
    named_fields = dict()

    if form.initial:
        for field in form.fields:
            attribute = dict()
            attribute['str_value'] = str(form.initial[field])
            attribute['value'] = form.initial[field]
            attribute['input_id'] = form.auto_id % field
            attribute['label'] = form.fields[field].label
            attribute['help_text'] = form.fields[field].help_text
            attribute['is_required'] = form.fields[field].required
            attribute['type'] = form.fields[field].widget.input_type
            named_fields[field] = attribute
    return named_fields
